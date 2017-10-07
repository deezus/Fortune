from django.db import models
from datetime import datetime

class User(models.Model):
    id = models.AutoField(primary_key=True)
    pseudo = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Fortune(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=1000)
    score = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date =  models.DateField(default=datetime.now)
