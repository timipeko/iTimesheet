# Generated by Django 2.1.7 on 2019-03-23 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0007_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='project',
        ),
        migrations.DeleteModel(
            name='Note',
        ),
    ]
