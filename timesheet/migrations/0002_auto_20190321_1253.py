# Generated by Django 2.1.7 on 2019-03-21 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name_plural': 'entries'},
        ),
        migrations.AddField(
            model_name='entry',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
