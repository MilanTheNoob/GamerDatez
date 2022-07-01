# Generated by Django 4.0.5 on 2022-06-27 08:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_profile_profileimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('users', models.TextField(blank=True)),
                ('messages', models.TextField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]