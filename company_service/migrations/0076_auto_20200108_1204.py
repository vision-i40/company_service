# Generated by Django 2.2.7 on 2020-01-08 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company_service', '0075_auto_20200108_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stateevent',
            name='production_line',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='state_events', to='company_service.ProductionLine'),
        ),
    ]
