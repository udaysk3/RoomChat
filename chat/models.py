from django.db import models
import datetime

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=10000)

class Message(models.Model):
    value = models.CharField(max_length=100000)
    time = models.CharField(max_length=1000000)
    user = models.CharField(max_length=1000)
    room = models.CharField(max_length=10000)