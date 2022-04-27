from lib2to3.pgen2 import token
from django.db import models

class Power(models.Model):
     date = models.DateField(auto_now_add=False)
     number = models.IntegerField(default=0)

class Bill(models.Model):
     name = models.CharField(max_length=255)
     price = models.IntegerField(default = 0)
     date = models.DateField(auto_now_add=True)
     owner = models.IntegerField(default = 0)
     payer = models.IntegerField(default = 0)
     status = models.IntegerField(default = 0)


