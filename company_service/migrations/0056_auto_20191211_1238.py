# Generated by Django 2.2.7 on 2019-12-11 12:38

from django.db import migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('company_service', '0055_auto_20191210_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='productionchart',
            name='created',
            field=model_utils.fields.AutoCreatedField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
        migrations.AddField(
            model_name='productionchart',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='modified'),
        ),
    ]
