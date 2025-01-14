# Generated by Django 5.0.4 on 2024-05-09 11:10

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('coid', models.AutoField(primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('lid', models.AutoField(primary_key=True, serialize=False)),
                ('postcode', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone', models.CharField(max_length=20)),
                ('street_name', models.CharField(max_length=255)),
                ('house_number', models.CharField(max_length=10)),
                ('date_of_birth', models.DateField(default=datetime.date(2000, 1, 1))),
                ('picture', models.URLField(default='http://t1.gstatic.com/licensed-image?q=tbn:ANd9GcR0NrOJEpfjkM0zxD-aO9b-bWqW3mhY57jPMg3aSbxTYO__R4jOvx8T2Oa7Fm9yxXOGg4B_ns3SZaZGCiBOPQw')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.country')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.location')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('eid', models.AutoField(primary_key=True, serialize=False)),
                ('place_of_work', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('rid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('role', models.CharField(max_length=100)),
                ('may_be_contacted', models.BooleanField(default=False)),
                ('Profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile')),
            ],
        ),
    ]
