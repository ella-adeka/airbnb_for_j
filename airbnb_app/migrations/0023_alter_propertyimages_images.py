# Generated by Django 4.0.4 on 2022-05-20 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airbnb_app', '0022_alter_property_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyimages',
            name='images',
            field=models.FileField(upload_to='images/properties'),
        ),
    ]