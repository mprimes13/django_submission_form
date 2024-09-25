from django.db import models
from django.utils.translation import gettext_lazy as tl

# Create your models here.
class Personal(models.Model):
    name     = models.CharField(max_length=50,null=False)
    title    = models.CharField(max_length=50,null=False)
    age      = models.PositiveIntegerField()
    hometown = models.CharField(max_length=200)

