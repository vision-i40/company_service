# Generated by Django 2.2.5 on 2019-09-09 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_service', '0014_auto_20190909_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='stopcode',
            name='was_planned',
            field=models.BooleanField(default=False),
        ),
    ]
