# Generated by Django 3.0.2 on 2020-01-16 13:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company_service', '0084_delete_productionchart'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductionChart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('start_datetime', models.DateTimeField(blank=True, db_index=True, default=None, null=True)),
                ('end_datetime', models.DateTimeField(blank=True, db_index=True, default=None, null=True)),
                ('quantity', models.IntegerField(default=1)),
                ('event_type', models.CharField(choices=[('Production', 'Production'), ('Waste', 'Waste'), ('Rework', 'Rework')], db_index=True, default='Production', max_length=20)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company_service.Product')),
                ('production_line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company_service.ProductionLine')),
                ('production_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company_service.ProductionOrder')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
