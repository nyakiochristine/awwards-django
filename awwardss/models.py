from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
import datetime as dt
from cloudinary.models import CloudinaryField

# Create your models here.
#profile,#post #rating


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    profile_picture = models.
    