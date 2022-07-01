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

    date_requests = models.TextField(default='[]')
    accepting_messages = models.CharField(default='', max_length=36)
    messages = models.TextField(default='[]')

    def __str__(self):
        return self.user.username

class Chat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    admin = models.IntegerField(default=-1)

    users = models.TextField(blank=True)
    messages = models.TextField(blank=True)

    def __str__(self):
        return "Message group created by User #" + str(self.admin)
