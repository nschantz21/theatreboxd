# Generated by Django 4.2.7 on 2023-12-04 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0004_alter_agent_date_of_birth'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Roles',
            new_name='Role',
        ),
    ]