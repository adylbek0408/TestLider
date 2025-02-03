from django.db import models

from django.contrib.auth.models import User

from main.models import Package


class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telegram_id = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username


class Client(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новый'),
        ('processing', 'В обработке'),
        ('no_answer', 'Не дозвон'),
        ('thinking', 'Думает'),
        ('rejected', 'Отклонено'),
        ('success', 'Успешно'),
    ]

    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    package = models.ForeignKey(Package, on_delete=models.SET_NULL, null=True, verbose_name='Выбранный пакет')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name='Статус')
    manager = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Менеджер')
    description = models.TextField(blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return f"{self.full_name} - {self.get_status_display()}"

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
