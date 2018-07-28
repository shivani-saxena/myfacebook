from django.db import models

# Create your models here.
class User(models.Model):
    email=models.CharField(max_length=100,primary_key=True)
    pwd=models.CharField(max_length=20)
    name=models.CharField(max_length=30)
    gender=models.CharField(max_length=20)

class Friend(models.Model):
    id=models.AutoField(primary_key=True)
    sender=models.CharField(max_length=100)
    rec=models.CharField(max_length=100)
    status=models.IntegerField()

class Wpost(models.Model):
   id=models.AutoField(primary_key=True)
   sender=models.CharField(max_length=100)
   msg=models.CharField(max_length=500)


class Data(models.Model):
   id=models.AutoField(primary_key=True)
   state=models.CharField(max_length=100)
   city=models.CharField(max_length=100)

#class Profile(models.Model):
    #pic=models.ImageField(upload_to='pic/%y%m%d', blank=True, null=True)
class Player_Profile(models.Model):
    name=models.CharField(max_length=50, null=True)
    email=models.EmailField(max_length=50)
    #profile_picture=models.ImageField(upload_to='profile_picture/%y%m%d', blank=True, null=True)
    profile_picture=models.ImageField(upload_to='profile_picture/%y%m%d', blank=True, null=True)
    age = models.IntegerField()
