# Generated by Django 3.2.9 on 2021-11-21 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_remove_blognote_slug'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogNote',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
