from django.db import models

# Create your models here.

class Info(models.Model):

    def __str__(self):
       return self.email

    name   = models.CharField(max_length=64)
    last_name    = models.CharField(max_length=64)
    date_of_birth = models.IntegerField(default=0)

    contacts     = models.CharField(max_length=64)
    email      = models.CharField(max_length=64)

    jabber         = models.CharField(max_length=64)
    skype         = models.CharField(max_length=64)
    other_contacts         = models.TextField()
    bio         = models.TextField()
