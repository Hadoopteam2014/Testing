from django.db import models

# Create your models here.

class userprofile(models.Model):
     Userids = models.CharField(max_length=200,primary_key=True)
     firstname = models.CharField(max_length=500)
     lastname = models.CharField(max_length=500)
     location = models.CharField(max_length=500)
     numconnections = models.IntegerField()
     interests = models.TextField(max_length=3000)

class Userskill(models.Model):
     Userids = models.CharField(max_length=200)
     skillid= models.IntegerField()
     skillname = models.CharField(max_length=500)
     
class usereducation(models.Model):
     Userids = models.CharField(max_length=200)
     eduid=models.BigIntegerField(primary_key=True)
     school = models.CharField(max_length=500)
     degree = models.CharField(max_length=500)
     startDate = models.CharField(max_length=500)
     endDate = models.CharField(max_length=500)
     fieldofstudy = models.CharField(max_length=500)

class usergroup(models.Model):
     Userids = models.CharField(max_length=500)
     groupid = models.CharField(max_length=200)
     groupname =models.TextField(max_length=3000)

class userposition(models.Model):
     ids = models.CharField(max_length=200)
     companyid = models.BigIntegerField(primary_key=True)
     compname = models.CharField(max_length=500)
    
class groups(models.Model):
     groupid = models.BigIntegerField()
     groupname = models.CharField(max_length=200)      

class company(models.Model):
     companyid=models.BigIntegerField(primary_key=True)
     updateKey = models.CharField(max_length=500)
     timestamp = models.CharField(max_length=500)
     numLikes = models.BigIntegerField()
     updatecontent = models.TextField(max_length=5000)
     updatecomments = models.TextField(max_length=5000)






