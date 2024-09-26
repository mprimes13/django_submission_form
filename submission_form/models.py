from django.db import models
from django.utils.translation import gettext_lazy as tl

TITLES = {
    'Mrs.': 'Mrs.',
    'Mr.':  'Mr.',
    'Ms.':  'Ms.',
    'Mx.':  'Mx.',
    '':     ''
}

# Create your models here.
class Personal(models.Model):
    name     = models.CharField(max_length=50,null=False,blank=False)
    title    = models.CharField(max_length=50,null=False,blank=False,choices=TITLES)
    age      = models.PositiveIntegerField(default=0)
    hometown = models.CharField(max_length=200,null=True,blank=True)

