# Generated by Django 4.0.4 on 2022-05-20 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airbnb_app', '0020_alter_property_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='image',
            field=models.FileField(blank=True, upload_to='properties'),
        ),
    ]