# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('municipality', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=1000)),
                ('case', models.SmallIntegerField(choices=[(1, 'Abandono en la calle'), (2, 'Exposición a temperaturas extremas'), (3, 'Falta de agua'), (4, 'Falta de comida'), (5, 'Violencia'), (6, 'Venta ambulante')])),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('lng', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('directions', models.TextField(max_length=200, null=True)),
                ('status', models.SmallIntegerField(choices=[(1, 'Reportada'), (2, 'Consolidada'), (3, 'Verificada'), (4, 'Cerrada'), (5, 'Desechada')])),
                ('gender', models.SmallIntegerField(choices=[(1, 'Macho'), (2, 'Hembra')])),
                ('wounded', models.BooleanField(choices=[(True, 'Sí'), (False, 'No')])),
                ('color', models.TextField(choices=[(1, 'marron'), (2, 'amarillo'), (3, 'blanco'), (4, 'gris'), (5, 'manchado')])),
                ('animal_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complaint.AnimalType')),
                ('municipality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='municipality.Municipality')),
            ],
        ),
        migrations.CreateModel(
            name='ComplaintImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='complaints/')),
                ('complaint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complaint.Complaint')),
            ],
        ),
    ]
