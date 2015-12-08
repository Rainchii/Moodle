# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=120)),
                ('pregunta1', models.CharField(max_length=120)),
                ('respuesta1', models.CharField(max_length=120)),
                ('pregunta2', models.CharField(max_length=120)),
                ('respuesta2', models.CharField(max_length=120)),
                ('pregunta3', models.CharField(max_length=120)),
                ('respuesta3', models.CharField(max_length=120)),
                ('pregunta4', models.CharField(max_length=120)),
                ('respuesta4', models.CharField(max_length=120)),
                ('pregunta5', models.CharField(max_length=120)),
                ('respuesta5', models.CharField(max_length=120)),
            ],
            options={
                'verbose_name_plural': 'examen',
            },
        ),
    ]
