# Generated by Django 2.2.4 on 2019-08-31 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_service', '0004_auto_20190831_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='slug',
            field=models.SlugField(),
        ),
    ]
