# Generated by Django 4.1.3 on 2022-12-29 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Artist', '0004_artisttable_genre_artisttable_language_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artisttable',
            name='manger',
            field=models.BooleanField(blank=True),
        ),
    ]