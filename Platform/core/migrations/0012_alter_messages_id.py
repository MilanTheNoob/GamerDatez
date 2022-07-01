# Generated by Django 4.0.5 on 2022-06-27 14:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_messages_delete_chat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
