from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models

import os
# Create your models here.

class User(AbstractUser):
    pass

class Message(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(default=datetime.now(), blank=True)