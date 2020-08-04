from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):

    username = models.EmailField(max_length=120, unique=True,null=True)

    USERNAME_FIELD = 'username'
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
