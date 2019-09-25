from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    token = models.CharField(null = True, blank = True, max_length = 20)
    activation = models.CharField(null = True, blank = True, max_length = 20)