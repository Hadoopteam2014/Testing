from django.db import models

class UserProfile(models.Model):
     UserId=models.BigIntegerField(primary_key=True)
     FirstName=models.CharField(max_length=100)
     LastName=models.CharField(max_length=100)
     Name=models.CharField(max_length=100)
     RelationStatus=models.CharField(max_length=100)
     Gender=models.CharField(max_length=100)
     Religion=models.CharField(max_length=100)
     Birthday=models.CharField(max_length=100)
     CurrentLoc=models.CharField(max_length=100)
     HomeTown=models.CharField(max_length=100)
     email=models.CharField(max_length=100)

class friendsprofile(models.Model):
     UserId=models.BigIntegerField(primary_key=True)
     frndId=models.BigIntegerField()
     FirstName=models.CharField(max_length=100)
     LastName=models.CharField(max_length=100)
     Name=models.CharField(max_length=100)
     RelationStatus=models.CharField(max_length=100)
     Gender=models.CharField(max_length=100)
     Religion=models.CharField(max_length=100)
     Birthday=models.CharField(max_length=100)
     CurrentLoc=models.CharField(max_length=100)
     HomeTown=models.CharField(max_length=100)
     email=models.CharField(max_length=100)

class user_likes(models.Model):
    user_id=models.BigIntegerField()
    likes_id=models.BigIntegerField()
    likes_category=models.CharField(max_length=200)
    likes_name=models.CharField(max_length=200)
class ids(models.Model):
    userid=models.BigIntegerField()
    friendsid=models.BigIntegerField()
class user_educations(models.Model):
    user_id=models.BigIntegerField()
    school_id=models.BigIntegerField(primary_key=True)
    school_name=models.CharField(max_length=200)
    school_type=models.CharField(max_length=200)
class friends_interest(models.Model):
    user_id=models.BigIntegerField()
    interest_category=models.CharField(max_length=200)
    interest_name=models.CharField(max_length=200)
class friends_location(models.Model):
    user_id=models.BigIntegerField()
    frnd_id=models.BigIntegerField()
    latitude=models.DecimalField(max_digits=30,decimal_places=3)
    longitude=models.DecimalField(max_digits=30,decimal_places=3)
class work_history(models.Model):
    user_id=models.BigIntegerField()
    emp_id=models.BigIntegerField(primary_key=True)
    emp_name=models.CharField(max_length=200)
     
     
       
     
 
