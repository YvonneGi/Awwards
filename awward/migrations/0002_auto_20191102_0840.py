# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-02 08:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('awward', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design', models.IntegerField()),
                ('usability', models.IntegerField()),
                ('content', models.IntegerField()),
                ('total', models.IntegerField()),
                ('avg', models.IntegerField(null=True)),
                ('comment', models.TextField(null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='awward.Project')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='rate',
            name='project',
        ),
        migrations.RemoveField(
            model_name='rate',
            name='username',
        ),
        migrations.DeleteModel(
            name='Rate',
        ),
    ]
