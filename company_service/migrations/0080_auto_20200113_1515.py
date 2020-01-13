# Generated by Django 3.0.2 on 2020-01-13 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company_service', '0079_productionchart_event_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availability',
            name='production_line',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='availabilities', to='company_service.ProductionLine'),
        ),
    ]
