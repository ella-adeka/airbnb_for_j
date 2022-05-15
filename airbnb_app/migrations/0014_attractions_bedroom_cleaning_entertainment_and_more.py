# Generated by Django 4.0.4 on 2022-05-13 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('airbnb_app', '0013_rename_highlght_highlights_highlight'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attractions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amenity', models.CharField(default='', max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Attractions',
            },
        ),
        migrations.CreateModel(
            name='Bedroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amenity', models.CharField(default='', max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Bedroom',
            },
        ),
        migrations.CreateModel(
            name='Cleaning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amenity', models.CharField(default='', max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Cleaning',
            },
        ),
        migrations.CreateModel(
            name='Entertainment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amenity', models.CharField(default='', max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Entertainment',
            },
        ),
        migrations.CreateModel(
            name='Facilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amenity', models.CharField(default='', max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Facilities',
            },
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amenity', models.CharField(default='', max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Family',
            },
        ),
        migrations.CreateModel(
            name='HeatingAndCooling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amenity', models.CharField(default='', max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Heating And Cooling',
            },
        ),
        migrations.CreateModel(
            name='InternetAndOffice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amenity', models.CharField(default='', max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Internet And Office',
            },
        ),
        migrations.CreateModel(
            name='Outdoors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amenity', models.CharField(default='', max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Outdoors',
            },
        ),
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amenity', models.CharField(default='', max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Parking',
            },
        ),
        migrations.CreateModel(
            name='Safety',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amenity', models.CharField(default='', max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Safety',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amenity', models.CharField(default='', max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.AlterModelOptions(
            name='reviews',
            options={'verbose_name_plural': 'Reviews'},
        ),
        migrations.CreateModel(
            name='PropertyImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='property')),
                ('property', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='airbnb_app.property')),
            ],
        ),
    ]
