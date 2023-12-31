# Generated by Django 4.2.7 on 2023-12-01 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0002_production_venue_alter_agent_date_of_death'),
    ]

    operations = [
        migrations.AddField(
            model_name='production',
            name='preview_dates',
            field=models.DateField(blank=True, null=True, verbose_name='previews date'),
        ),
        migrations.AlterField(
            model_name='production',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='closing date'),
        ),
    ]
