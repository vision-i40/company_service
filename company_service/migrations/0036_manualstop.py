# Generated by Django 2.2.5 on 2019-10-21 18:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('company_service', '0035_auto_20190923_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManualStop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('start_datetime', models.DateTimeField(db_index=True, default=None)),
                ('end_datetime', models.DateTimeField(db_index=True, default=None)),
                ('state', models.CharField(default='Off', editable=False, max_length=3)),
                ('production_line', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company_service.ProductionLine')),
                ('state_event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='company_service.StateEvent')),
                ('stop_code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company_service.StopCode')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
