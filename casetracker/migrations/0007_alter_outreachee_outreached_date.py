# Generated by Django 3.2.6 on 2021-09-21 19:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casetracker', '0006_auto_20210921_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outreachee',
            name='outreached_date',
            field=models.DateField(default=datetime.date(2021, 9, 21)),
        ),
    ]
