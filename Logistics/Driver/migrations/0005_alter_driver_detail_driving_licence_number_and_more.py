# Generated by Django 4.0.6 on 2022-07-22 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Driver', '0004_remove_driver_detail_driving_licence_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver_detail',
            name='driving_licence_number',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='driver_detail',
            name='vehicle_registration_number',
            field=models.ImageField(upload_to='images/'),
        ),
    ]