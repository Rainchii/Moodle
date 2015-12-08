# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=25)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=125, verbose_name=b'Apellidos')),
                ('email', models.EmailField(max_length=60, verbose_name=b'E-mail')),
            ],
        ),
    ]
