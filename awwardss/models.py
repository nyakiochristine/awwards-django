from gzip import READ
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
import datetime as dt
from cloudinary.models import CloudinaryField
# Create your models here.
#profile,#post #rating


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    profile_picture = models.CloudinaryField()
    bio= models.TextField(max_length=355,default='my bio',blank=True)
    name = models.CharField(max_length=65,blank=True)
    location = models.CharField(max_length=65,blank=True)
    
    
    
    
    
    
class Post(models.Model):
    title = models.CharField(max_length=140)
    url = models.URLField(max_length=200)
    description = models.TextField(max_length=500)
    technologies = models.CharField(max_length=100, blank=True)
    photo = models.CloudinaryField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    date = models.DateTimeField(auto_now_add=True, blank=True)
    
    
    def __str__(self):
        return f'{self.title}'
    
    def  delete_post(self):
        self.delete()
        
        
    