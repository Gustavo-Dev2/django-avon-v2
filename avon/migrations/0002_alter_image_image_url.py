# Generated by Django 5.1.1 on 2024-09-08 08:58

import avon.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_url',
            field=models.ImageField(blank=True, upload_to='images/', validators=[avon.models.Image.validate_image]),
        ),
    ]
