from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=70 )
    email = models.CharField(max_length=70)
    password = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=15)
    profile_picture = models.CharField(max_length=200)

    def save(self ,*args , **kwargs):
        if self.username or not self.username:
            self.username = self.email
        super(User , self).save(*args , **kwargs)

    def __str__(self):
        return self.email