from django.db import models

# Create your models here.

class UserInfo:
    name = str
    email = str
    image = str

class account(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    email = models.EmailField(blank=True)