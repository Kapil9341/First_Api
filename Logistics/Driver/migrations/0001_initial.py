# Generated by Django 4.0.6 on 2022-07-22 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('address', models.CharField(max_length=300)),
                ('vehicle_registration_number', models.CharField(max_length=100)),
                ('driving_licence_number', models.CharField(max_length=100)),
                ('registration_card_photo', models.FileField(upload_to='')),
                ('driving_licence_photo', models.FileField(upload_to='')),
            ],
        ),
    ]
