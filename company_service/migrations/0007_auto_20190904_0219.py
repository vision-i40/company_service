# Generated by Django 2.2.4 on 2019-09-04 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_service', '0006_auto_20190903_2349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unitofmeasurement',
            old_name='is_global',
            new_name='is_default',
        ),
        migrations.RemoveField(
            model_name='unitofmeasurement',
            name='description',
        ),
        migrations.AlterField(
            model_name='unitofmeasurement',
            name='conversion_factor',
            field=models.FloatField(default=1.0),
        ),
        migrations.DeleteModel(
            name='ProductConversion',
        ),
    ]
