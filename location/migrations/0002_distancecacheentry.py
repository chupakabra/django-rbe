# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-08 20:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DistanceCacheEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('distance_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='distance_to', to=settings.AUTH_USER_MODEL)),
                ('user_source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_source', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]