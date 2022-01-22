# Generated by Django 3.2.8 on 2021-10-24 08:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=60, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='BlogNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, unique=True, verbose_name='Название')),
                ('img', models.ImageField(blank=True, upload_to='resources/images/%Y/%m/%d/', verbose_name='Изображение')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, default='', null=True, unique=True, verbose_name='URL')),
                ('txt', models.TextField(verbose_name='Текст')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_date', models.DateField(auto_now_add=True, verbose_name='Дата изменения')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('category', models.ManyToManyField(to='blog.Category', verbose_name='Категории')),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блоги',
                'ordering': ('-update_date', 'title'),
            },
        ),
    ]
