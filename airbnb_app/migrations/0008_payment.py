# Generated by Django 4.0.4 on 2022-06-22 22:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('airbnb_app', '0007_rename_max_days_property_min_days'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.FloatField()),
                ('date_paid', models.DateTimeField(auto_now_add=True)),
                ('booking', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='airbnb_app.booking')),
                ('user', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
