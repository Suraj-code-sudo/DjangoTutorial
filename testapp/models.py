from django.db import models

# Create your models here.

class Voters(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    is_voted = models.BooleanField(default=False)
