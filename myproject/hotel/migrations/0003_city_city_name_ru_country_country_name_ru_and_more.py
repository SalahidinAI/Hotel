# Generated by Django 5.1.4 on 2025-01-01 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_city_city_name_en_city_city_name_tr_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='city_name_ru',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='country',
            name='country_name_ru',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_name_ru',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
