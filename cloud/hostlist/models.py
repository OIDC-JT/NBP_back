from django.db import models

# Create your models here.
class Gethost(models.Model):
    username = models.TextField(max_length=100)