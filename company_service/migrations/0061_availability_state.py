# Generated by Django 2.2.7 on 2019-12-17 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_service', '0060_auto_20191217_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='availability',
            name='state',
            field=models.CharField(db_index=True, default='On', max_length=3),
        ),
    ]
