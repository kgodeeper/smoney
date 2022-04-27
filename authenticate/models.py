import time
import django
from django.db import models
from django.utils import timezone
# Create your models here.
# Create your models here.
class admin(models.Model):
     password  = models.CharField(max_length=256)
     token     = models.CharField(max_length=500, blank=True)
     token_due = models.DateTimeField(default=timezone.now)