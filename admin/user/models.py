from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):

    username = models.CharField(max_length=120, unique=True,null=True)

    USERNAME_FIELD = 'username'
    email = models.EmailField(max_length=254,unique=True)
