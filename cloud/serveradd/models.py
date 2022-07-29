from django.db import models

# Create your models here.

class Serveradd(models.Model):
    servertype = models.TextField(max_length=100)
    servername = models.TextField(max_length=100)