# Generated by Django 4.0.6 on 2022-07-06 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_rename_genre_genremodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ebook',
            name='genre',
        ),
    ]
