# Generated by Django 2.2.6 on 2019-11-20 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company_service', '0050_auto_20191118_1252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turn',
            name='production_line',
        ),
    ]