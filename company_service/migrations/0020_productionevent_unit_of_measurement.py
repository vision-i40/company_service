# Generated by Django 2.2.5 on 2019-09-10 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company_service', '0019_auto_20190910_0029'),
    ]

    operations = [
        migrations.AddField(
            model_name='productionevent',
            name='unit_of_measurement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='company_service.UnitOfMeasurement'),
        ),
    ]