from django.db import models
from customuser.models import CustomUser

class Group(models.Model):
    name         = models.CharField(max_length=200)
    description  = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    slug         = models.SlugField()
    creator      = models.CharField(max_length=200)
    members      = models.ManyToManyField(CustomUser,related_name="members")

    def __str__(self):
        return self.name



