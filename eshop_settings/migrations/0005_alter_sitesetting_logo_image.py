# Generated by Django 4.0.3 on 2022-04-20 10:47

from django.db import migrations, models
import eshop_settings.models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_settings', '0004_sitesetting_logo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesetting',
            name='logo_image',
            field=models.ImageField(blank=True, null=True, upload_to=eshop_settings.models.upload_image_path, verbose_name='تصویر لوگو'),
        ),
    ]
