# Generated by Django 2.1.7 on 2019-03-21 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0005_auto_20190321_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]