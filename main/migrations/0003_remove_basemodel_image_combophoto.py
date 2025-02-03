# Generated by Django 5.1.4 on 2025-01-23 18:07

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_ajy_options_alter_articleornews_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basemodel',
            name='image',
        ),
        migrations.CreateModel(
            name='ComboPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rich', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='', verbose_name='Картинка:')),
                ('combo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='combo_photos', to='main.combo', verbose_name='Комбо')),
            ],
            options={
                'verbose_name': 'Фото комбо',
                'verbose_name_plural': 'Фото комбо',
            },
        ),
    ]
