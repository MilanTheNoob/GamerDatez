# Generated by Django 4.0.5 on 2022-07-03 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_remove_profile_sessionid_profile_messages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_requests',
            field=models.TextField(default='[]'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='messages',
            field=models.TextField(default='[]'),
        ),
    ]