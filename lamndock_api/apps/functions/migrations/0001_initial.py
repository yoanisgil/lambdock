# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-30 20:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Function',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('timeout', models.FloatField(help_text='Maximum function execution time in milliseconds')),
            ],
        ),
        migrations.CreateModel(
            name='FunctionVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('version', models.CharField(max_length=10)),
                ('function', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='functions.Function')),
            ],
        ),
        migrations.CreateModel(
            name='Stack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('docker_image', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='function',
            name='stack',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='functions.Stack'),
        ),
        migrations.AlterUniqueTogether(
            name='functionversion',
            unique_together=set([('id', 'version')]),
        ),
    ]