# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ong', '0001_initial'),
        ('complaint', '0001_initial'),
        ('ong', '0001_initial'),
        ('naturalUser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adopt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('gender', models.SmallIntegerField(choices=[(1, 'Macho'), (2, 'Hembra')])),
                ('description', models.TextField(max_length=1000)),
                ('color', models.IntegerField(choices=[(1, 'marron'), (2, 'amarillo'), (3, 'blanco'), (4, 'gris'), (5, 'manchado')])),
                ('estimated_age', models.PositiveSmallIntegerField()),

                ('first_day', models.DateTimeField(auto_now_add=True)),

                ('animal_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complaint.AnimalType')),
                ('ong_responsable', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ong.ONG')),
            ],
        ),
        migrations.CreateModel(
            name='AnimalImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='animals/')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animals.Animal')),
            ],
        ),
        migrations.AddField(
            model_name='adopt',
            name='animal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animals.Animal'),
        ),
        migrations.AddField(
            model_name='adopt',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='naturalUser.NaturalUser'),
        ),
    ]
