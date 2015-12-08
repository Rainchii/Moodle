# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=25)),
                ('ciclo', models.CharField(max_length=25)),
                ('grupo', models.CharField(max_length=125)),
                ('capacidad', models.IntegerField(default=0)),
            ],
        ),
    ]
