# Generated by Django 5.0.4 on 2024-05-09 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.URLField(),
        ),
    ]
