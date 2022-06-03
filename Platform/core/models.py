from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
from django_countries.fields import CountryField
from django.core.validators import MaxValueValidator, MinValueValidator

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    games = (('mc', 'Minecraft'),('fortnite', 'Fortnite'),('valorant', 'Valorant'),('lol', 'League of Legends'),
    ('cod', 'Call of Duty'),('gta', 'Grand Theft Auto'),('apex', 'Apex Legends'),('csgo', 'Counter Strike: Global Offensive'),
    ('dbd', 'Dead by Daylight'),('wow', 'World of Warcraft'),('eft', 'Escape from Tarkov'),('genshin', 'Genshin Impact'),
    ('rss', 'Rainbow Six Seige'),('overwatch', 'Overwatch'),('pubg', 'PUBG'),('dota', 'Dota'),('amogus', 'Among Us'),
    ('phasma', 'Phasmophobia'),('fifa', 'Fifa'),('destiny', 'Destiny'),('eldenring', 'Elden Ring'),('roblox', 'Roblox'),
    ('candycrush', 'Candy Crush'),('rust', 'rust'),('wot', 'World of Tanks'),('vrchat', 'VR Chat'),('halo', 'Halo'),
    ('rdr', 'Red Dead Redemption'),('sot', 'Sea Of Thieves'),('nba', 'NBA'),)

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

    fav_game = models.CharField(max_length=10, choices=games, default=1)
    sec_fav_game = models.CharField(max_length=10, choices=games, default=1)
    third_fav_game = models.CharField(max_length=10, choices=games, default=1)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    location = models.CharField(max_length=100, default="My basement")
    created_at = models.DateTimeField(default=datetime.now)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user
