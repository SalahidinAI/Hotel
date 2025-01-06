# Generated by Django 5.1.4 on 2025-01-02 06:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0006_roomimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_city', to='hotel.city'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_country', to='hotel.country'),
        ),
        migrations.AlterField(
            model_name='roomimage',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_images', to='hotel.room'),
        ),
    ]
