from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
from django_countries.fields import CountryField
from django.core.validators import MaxValueValidator, MinValueValidator

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()

    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)

    sex = models.CharField(max_length=1, default=1)
    preference = models.CharField(max_length=1, default=1)

    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='default-profile-picture.jpg')
    age = models.IntegerField(default=18)
    birth_date = models.DateTimeField(default=datetime.now)
    country = CountryField(default='US')

    fav_game = models.TextField(default='Minecraft')
    sec_fav_game = models.TextField(default='Fortnite')
    third_fav_game = models.TextField(default='Call of Duty')

    date_requests = models.TextField(default='[]')
    accepting_messages = models.TextField(default='')
    messages = models.TextField(default='[]')
    dates_updated = models.DateTimeField(default=datetime.now)
    user_setup = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Chat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    admin = models.IntegerField(default=-1)

    users = models.TextField(blank=True)
    messages = models.TextField(blank=True)

    def __str__(self):
        return self.id
