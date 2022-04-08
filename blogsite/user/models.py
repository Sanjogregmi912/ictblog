from django.db import models

# Create your models here.
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User

class Auth_user(AbstractBaseUser):
    Is_writer = models.CharField(max_length=12,unique=True)
    USERNAME_FIELD = 'Is_writer'
