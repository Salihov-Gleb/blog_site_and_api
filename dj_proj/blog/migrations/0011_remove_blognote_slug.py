# Generated by Django 3.2.9 on 2021-11-16 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_blognote_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blognote',
            name='slug',
        ),
    ]
