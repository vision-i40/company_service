# Generated by Django 2.2.4 on 2019-09-06 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company_service', '0008_turn_days_week'),
    ]

    operations = [
        migrations.RenameField(
            model_name='turn',
            old_name='days_week',
            new_name='days_of_week',
        ),
        migrations.AlterField(
            model_name='turn',
            name='turn_scheme',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company_service.TurnScheme'),
        ),
    ]
