from django.db import models 
class Userprofile (models.Model):
    userid = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    Description = models.CharField(max_length=200)
    screen_name = models.CharField(max_length=200)
class Frnds(models.Model):
    userid = models.BigIntegerField()
    frndid = models.BigIntegerField()
    frndname =  models.CharField(max_length=200)
    location = models.CharField(max_length=200)
class Followers(models.Model):
    userid = models.BigIntegerField()
    followerdid = models.BigIntegerField()
    followername =  models.CharField(max_length=500)
    location = models.CharField(max_length=200)
class Favourites(models.Model):
    favourid = models.BigIntegerField()
    favourname = models.CharField(max_length=500)
