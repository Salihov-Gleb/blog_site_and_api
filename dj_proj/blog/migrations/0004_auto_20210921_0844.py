# Generated by Django 3.2.7 on 2021-09-21 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blognote_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blognote',
            name='category',
        ),
        migrations.AddField(
            model_name='blognote',
            name='category',
            field=models.ManyToManyField(to='blog.Category', verbose_name='Категории'),
        ),
        migrations.AlterField(
            model_name='blognote',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата'),
        ),
    ]