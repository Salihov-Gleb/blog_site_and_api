# Generated by Django 3.2.7 on 2021-09-16 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210916_1252'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blognote',
            options={'ordering': ('-date', 'title'), 'verbose_name': 'Блог', 'verbose_name_plural': 'Блоги'},
        ),
    ]
