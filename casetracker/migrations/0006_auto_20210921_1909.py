# Generated by Django 3.2.6 on 2021-09-21 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casetracker', '0005_alter_outreachee_zipcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outreachee',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='outreachee',
            name='street',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
