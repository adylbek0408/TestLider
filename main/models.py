from django.db import models
from ckeditor.fields import RichTextField


class BaseModel(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название:', null=True, blank=True)
    rich = RichTextField(verbose_name='Описание', blank=True, null=True)
    date = models.DateTimeField(verbose_name='Дата:', null=True, blank=True)
    image = models.ImageField(verbose_name='Картинка:', null=True, blank=True)


class Ajy(models.Model):
    name = models.CharField(max_length=100, verbose_name='ФИО:')
    bio = models.TextField(verbose_name='Биография:')
    image = models.ImageField(verbose_name='Фотография:')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ажы'
        verbose_name_plural = 'Ажы'


class CategoryPackage(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название:')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория пакета'
        verbose_name_plural = 'Категории пакетов'


class Package(models.Model):
    category = models.ForeignKey(CategoryPackage, on_delete=models.CASCADE, related_name='package_categories',
                                 verbose_name='Категория пакета:')
    ajy = models.ForeignKey(Ajy, on_delete=models.CASCADE, related_name='package_ajy',
                            verbose_name='Ажы башчылар::')
    name = models.CharField(max_length=155, verbose_name='Название:')
    description = models.TextField(verbose_name='Описание:', null=True, blank=True)
    start_tour = models.DateTimeField(verbose_name='Дата начало:')                             # ???db_index=True???
    end_tour = models.DateField(verbose_name='Дата конец:')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена (в долларах):')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пакет'
        verbose_name_plural = 'Пакеты'


class PhotoPackage(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='photo_packages',
                                verbose_name='Пакеты')
    image = models.ImageField(verbose_name='Картинка:')

    class Meta:
        verbose_name = 'Фото пакета'
        verbose_name_plural = 'Фото пакетов'


class Combo(BaseModel):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='packages',
                                verbose_name='Пакеты')
    COMBO_CHOICES = (
        ('FoodInfo', 'FoodInfo'),
        ('Requirements', 'Requirements'),
        ('Restrictions', 'Restrictions'),
        ('PlacesToVisit', 'PlacesToVisit'),
        ('YouGet', 'YouGet'),
    )
    combo_choices = models.CharField(max_length=100, choices=COMBO_CHOICES, verbose_name='Место:')

    class Meta:
        verbose_name = 'Комбо'
        verbose_name_plural = 'Комбо'


class ArticleOrNews(BaseModel):
    CHOICES = (
        ('Article', 'Article'),
        ('News', 'News'),

    )
    choices = models.CharField(max_length=100, choices=CHOICES, verbose_name='Место:')

    class Meta:
        verbose_name = 'Статья или новость'
        verbose_name_plural = 'Статьи или новости'


class Lesson(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='lesson_packages',
                                verbose_name='Пакеты')
    date = models.DateTimeField(verbose_name='Дата урока:')
    video_url = models.URLField(max_length=255, verbose_name='Ссылка на видео (YouTube):')
    description = models.TextField(verbose_name='Описание урока:')

    def __str__(self):
        return self.package.name

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

