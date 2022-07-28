# Generated by Django 4.0.6 on 2022-07-28 10:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Driver', '0018_alter_driver_detail_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver_detail',
            name='phone_number',
            field=models.CharField(blank=True, max_length=12, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 12 digits allowed.", regex='\x08(\\d|1[0-2])\x08')]),
        ),
    ]
