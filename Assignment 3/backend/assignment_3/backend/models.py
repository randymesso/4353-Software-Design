from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.db.models import IntegerField, Model

# Create your models here.

#profile model
class Profile(models.Model):
    fullname = models.CharField(max_length=50)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=9,validators=[RegexValidator(regex=r'^(^[0-9]{5}(?:-[0-9]{4})?$|^$)')])
    
    