# Generated by Django 4.1.5 on 2023-06-02 23:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corbeillepatient',
            name='dateSuppression_debut',
            field=models.DateField(default=datetime.datetime(2023, 6, 2, 23, 12, 41)),
        ),
        migrations.AlterField(
            model_name='corbeillepatient',
            name='dateSuppression_fin',
            field=models.DateField(default=datetime.datetime(2023, 7, 3, 0, 12, 41)),
        ),
    ]