# Generated by Django 4.0.5 on 2022-06-27 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_profile_date_requests_alter_profile_profileimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(default='default-profile-picture.jpg', upload_to='profile_images'),
        ),
    ]