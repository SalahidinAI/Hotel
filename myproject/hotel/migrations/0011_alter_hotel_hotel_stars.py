# Generated by Django 5.1.4 on 2025-01-06 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0010_alter_room_room_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='hotel_stars',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
    ]
