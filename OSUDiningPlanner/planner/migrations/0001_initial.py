# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 21:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('portion_size', models.CharField(max_length=200)),
                ('course', models.CharField(max_length=200)),
                ('ingredients', models.TextField()),
                ('requirement', models.CharField(max_length=200)),
                ('allergen', models.CharField(max_length=200)),
                ('calories', models.PositiveIntegerField(default=0)),
                ('total_fat', models.CharField(max_length=200)),
                ('saturated_fat', models.CharField(max_length=200)),
                ('trans_fat', models.CharField(max_length=200)),
                ('cholestrol', models.CharField(max_length=200)),
                ('sodium', models.CharField(max_length=200)),
                ('total_carbohydrates', models.CharField(max_length=200)),
                ('dietary_fiber', models.CharField(max_length=200)),
                ('sugars', models.CharField(max_length=200)),
                ('protein', models.CharField(max_length=200)),
                ('vitamin_a', models.CharField(max_length=200)),
                ('vitamin_c', models.CharField(max_length=200)),
                ('calcium', models.CharField(max_length=200)),
                ('iron', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=200)),
                ('address2', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('zipcode', models.PositiveIntegerField()),
                ('dining_style', models.CharField(blank=True, max_length=200, null=True)),
                ('icon_URL', models.URLField(blank=True, null=True)),
                ('photo_URL', models.URLField(blank=True, null=True)),
                ('thumbnail_URL', models.URLField(blank=True, null=True)),
                ('cuisines', models.CharField(max_length=200)),
                ('summary', models.TextField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('is_day_specific', models.BooleanField()),
                ('location_menu', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.Location'),
        ),
        migrations.AlterUniqueTogether(
            name='food',
            unique_together=set([('name', 'location')]),
        ),
    ]