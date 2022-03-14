from django.conf import settings
from django.db import models
from django.utils import timezone

from django.core.validators import RegexValidator, MinValueValidator
from django.db.models import IntegerField, Model

from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

#profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    
    fullname = models.CharField(max_length=50)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=9,validators=[RegexValidator(regex=r'^(^[0-9]{5}(?:-[0-9]{4})?$|^$)')])
    
    @receiver(post_save,sender=User)
    def create_user_profile(sender,instance, created, **kwards):
        if (created):
            Profile.objects.create(user=instance)
            
    def save_user_profile(sender,instance, **kwards):
        instance.profile.save()

#fuel quote model
class Fuel_Quote(models.Model):
    gallons_requested = models.IntegerField(default = 0, validators=[MinValueValidator(0)])
    delivery_address = models.CharField(max_length=100)
    delivery_date = models.DateField(auto_now = True)
    suggested_price = models.IntegerField(default = 0, validators=[MinValueValidator(0)])
    total_due = models.IntegerField(default = 0, validators=[MinValueValidator(0)])
    
#pricing module model
class Pricing_Module(models.Model):
    suggested_price = models.IntegerField(default = 0, validators=[MinValueValidator(0)])
    