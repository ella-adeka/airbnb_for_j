# Generated by Django 4.0.4 on 2022-05-13 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airbnb_app', '0014_attractions_bedroom_cleaning_entertainment_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property',
            options={'ordering': ('title',), 'verbose_name_plural': 'Properties'},
        ),
        migrations.AlterModelOptions(
            name='propertyimages',
            options={'verbose_name_plural': 'Property Images'},
        ),
        migrations.RenameField(
            model_name='property',
            old_name='bathroom_objects',
            new_name='bathroom',
        ),
        migrations.AddField(
            model_name='property',
            name='attractions',
            field=models.ManyToManyField(to='airbnb_app.attractions'),
        ),
        migrations.AddField(
            model_name='property',
            name='bedroom',
            field=models.ManyToManyField(to='airbnb_app.bedroom'),
        ),
        migrations.AddField(
            model_name='property',
            name='cleaning',
            field=models.ManyToManyField(to='airbnb_app.cleaning'),
        ),
        migrations.AddField(
            model_name='property',
            name='entertainment',
            field=models.ManyToManyField(to='airbnb_app.entertainment'),
        ),
        migrations.AddField(
            model_name='property',
            name='facilities',
            field=models.ManyToManyField(to='airbnb_app.facilities'),
        ),
        migrations.AddField(
            model_name='property',
            name='family',
            field=models.ManyToManyField(to='airbnb_app.family'),
        ),
        migrations.AddField(
            model_name='property',
            name='heating_and_cooling',
            field=models.ManyToManyField(to='airbnb_app.heatingandcooling'),
        ),
        migrations.AddField(
            model_name='property',
            name='internet_and_office',
            field=models.ManyToManyField(to='airbnb_app.internetandoffice'),
        ),
        migrations.AddField(
            model_name='property',
            name='kitchen_and_dining',
            field=models.ManyToManyField(to='airbnb_app.kitchenanddining'),
        ),
        migrations.AddField(
            model_name='property',
            name='outdoors',
            field=models.ManyToManyField(to='airbnb_app.outdoors'),
        ),
        migrations.AddField(
            model_name='property',
            name='parking',
            field=models.ManyToManyField(to='airbnb_app.parking'),
        ),
        migrations.AddField(
            model_name='property',
            name='safety',
            field=models.ManyToManyField(to='airbnb_app.safety'),
        ),
        migrations.AddField(
            model_name='property',
            name='services',
            field=models.ManyToManyField(to='airbnb_app.services'),
        ),
    ]
