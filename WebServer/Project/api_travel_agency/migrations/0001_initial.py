# Generated by Django 5.0 on 2024-01-12 11:49

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('auto_increment_id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('street', models.CharField(blank=True, max_length=256, null=True)),
                ('number', models.CharField(blank=True, max_length=256, null=True)),
                ('city', models.CharField(blank=True, max_length=256, null=True)),
                ('country', models.CharField(blank=True, max_length=256, null=True)),
                ('image_url', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('auto_increment_id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=256, null=True)),
                ('start_date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('price', models.CharField(blank=True, max_length=256, null=True)),
                ('free_slots', models.IntegerField(blank=True, null=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_travel_agency.location')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('auto_increment_id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('contact_name', models.CharField(blank=True, max_length=256, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=256, null=True)),
                ('holiday', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_travel_agency.holiday')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_travel_agency.location')),
            ],
        ),
    ]