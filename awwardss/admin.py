from django.contrib import admin
from . import models


admin.register(models.Profile)
admin.register(models.Post)
admin.register(models.Rating)

# Register your models here.
