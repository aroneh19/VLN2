# Generated by Django 5.0.4 on 2024-05-06 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_date_of_birth'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='lid',
            new_name='lid_id',
        ),
    ]