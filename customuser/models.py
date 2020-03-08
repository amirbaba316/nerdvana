from django.db import models
from django.contrib.auth.models import User

class CustomUser(User,models.Model):
    photo    = models.ImageField(upload_to='photos/%Y/%m/%d/')
    def __str__(self):
        return self.username
