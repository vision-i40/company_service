# Generated by Django 2.2.5 on 2019-10-21 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company_service', '0036_manualstop'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manualstop',
            name='state',
        ),
    ]
