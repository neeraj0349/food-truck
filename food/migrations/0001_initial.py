# Generated by Django 4.2.8 on 2023-12-09 18:11

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodTruck',
            fields=[
                ('location_id', models.IntegerField(primary_key=True, serialize=False)),
                ('applicant', models.CharField(max_length=255)),
                ('facility_type', models.CharField(max_length=255)),
                ('cnn', models.IntegerField()),
                ('location_description', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('block_lot', models.CharField(max_length=255)),
                ('block', models.CharField(max_length=255)),
                ('lot', models.CharField(max_length=255)),
                ('permit', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('food_items', models.TextField()),
                ('x', models.FloatField(blank=True, null=True)),
                ('y', models.FloatField(blank=True, null=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('schedule', models.CharField(max_length=255)),
                ('days_hours', models.CharField(max_length=255)),
                ('noi_sent', models.CharField(max_length=255)),
                ('approved', models.DateTimeField(blank=True, null=True)),
                ('received', models.DateField()),
                ('prior_permit', models.CharField(max_length=255)),
                ('expiration_date', models.DateTimeField(blank=True, null=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(max_length=255, srid=4326)),
                ('fire_prevention_districts', models.IntegerField(blank=True, null=True)),
                ('police_districts', models.IntegerField(blank=True, null=True)),
                ('supervisor_districts', models.IntegerField(blank=True, null=True)),
                ('zip_codes', models.IntegerField(blank=True, null=True)),
                ('neighborhoods_old', models.CharField(max_length=255)),
            ],
        ),
    ]
