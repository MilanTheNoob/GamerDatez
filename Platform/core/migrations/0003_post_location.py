# Generated by Django 4.0.4 on 2022-05-26 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_post_remove_profile_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='location',
            field=models.CharField(default='My basement', max_length=100),
        ),
    ]
