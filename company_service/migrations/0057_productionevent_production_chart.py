# Generated by Django 2.2.7 on 2019-12-11 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company_service', '0056_auto_20191211_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='productionevent',
            name='production_chart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='production_events', to='company_service.ProductionChart'),
        ),
    ]
