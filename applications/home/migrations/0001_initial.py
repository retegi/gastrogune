# Generated by Django 4.0.6 on 2022-07-24 20:46

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('documentName', models.CharField(blank=True, max_length=255, null=True)),
                ('documentDescription', models.CharField(blank=True, max_length=255, null=True)),
                ('templateType', models.CharField(blank=True, max_length=255, null=True)),
                ('locality', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('marks', models.CharField(blank=True, max_length=255, null=True)),
                ('physical', models.CharField(blank=True, max_length=255, null=True)),
                ('visual', models.CharField(blank=True, max_length=255, null=True)),
                ('auditive', models.FloatField(blank=True, max_length=255, null=True)),
                ('intellectual', models.FloatField(blank=True, max_length=255, null=True)),
                ('organic', models.FloatField(blank=True, max_length=255, null=True)),
                ('qualityAssurance', models.FloatField(blank=True, max_length=255, null=True)),
                ('tourismEmail', models.FloatField(blank=True, max_length=255, null=True)),
                ('web', models.FloatField(blank=True, max_length=255, null=True)),
                ('capacity', models.CharField(blank=True, max_length=255, null=True)),
                ('postalCode', models.CharField(blank=True, max_length=255, null=True)),
                ('restorationType', models.FloatField(blank=True, max_length=255, null=True)),
                ('restaurant', models.FloatField(blank=True, max_length=255, null=True)),
                ('bodega', models.CharField(blank=True, max_length=255, null=True)),
                ('latitudelongitude', models.CharField(blank=True, max_length=255, null=True)),
                ('latwgs84', models.FloatField(blank=True, max_length=255, null=True)),
                ('lonwgs84', models.CharField(blank=True, max_length=255, null=True)),
                ('municipality', models.CharField(blank=True, max_length=255, null=True)),
                ('municipalitycode', models.FloatField(blank=True, max_length=255, null=True)),
                ('territory', models.FloatField(blank=True, max_length=255, null=True)),
                ('territorycode', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.FloatField(blank=True, max_length=255, null=True)),
                ('countrycode', models.CharField(blank=True, max_length=255, null=True)),
                ('friendlyUrl', models.FloatField(blank=True, max_length=255, null=True)),
                ('physicalUrl', models.CharField(blank=True, max_length=255, null=True)),
                ('dataXML', models.FloatField(blank=True, max_length=255, null=True)),
                ('metadataXML', models.CharField(blank=True, max_length=255, null=True)),
                ('zipFile', models.CharField(blank=True, max_length=255, null=True)),
                ('_num', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
