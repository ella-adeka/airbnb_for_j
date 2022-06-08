# Generated by Django 4.0.4 on 2022-06-05 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airbnb_app', '0019_remove_booking_property_name_booking_property_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='reserved',
            field=models.BooleanField(default=False),
        ),
    ]