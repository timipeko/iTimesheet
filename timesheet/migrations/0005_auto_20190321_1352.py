# Generated by Django 2.1.7 on 2019-03-21 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0004_entry_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
