# Generated by Django 3.2.6 on 2021-09-22 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casetracker', '0013_auto_20210922_0336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertable',
            name='middle_initial',
            field=models.CharField(default='', max_length=1),
        ),
    ]
