# Generated by Django 4.2.7 on 2023-12-01 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='production',
            name='venue',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ratings.venue'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='agent',
            name='date_of_death',
            field=models.DateField(blank=True, null=True),
        ),
    ]
