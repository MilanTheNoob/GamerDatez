# Generated by Django 4.0.5 on 2022-06-27 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_chat_delete_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='admin',
            field=models.IntegerField(default=-1),
        ),
    ]