# Generated by Django 5.0.4 on 2024-05-06 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_rename_job_type_job_joid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='joid',
            new_name='jobtype',
        ),
    ]