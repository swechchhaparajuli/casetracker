# Generated by Django 3.2.6 on 2021-09-23 23:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('casetracker', '0014_alter_usertable_middle_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='enrolled_date',
            field=models.DateField(default=datetime.date(2021, 9, 23)),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='enrollment_key',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='outreachee',
            name='outreached_date',
            field=models.DateField(default=datetime.date(2021, 9, 23)),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('applcants', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='casetracker.applicant')),
                ('outreachees', models.ManyToManyField(to='casetracker.UserTable')),
            ],
        ),
    ]
