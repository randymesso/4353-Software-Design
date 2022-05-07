from django.conf import settings
from django.db import models
from django.utils import timezone

from django.core.validators import RegexValidator, MinValueValidator
from django.db.models import PositiveIntegerField, Model

from django.contrib.auth.models import AbstractUser

from django.dispatch import receiver
from django.db.models.signals import post_save

from .managers import CustomUserManager

# User model 
class UserCredentials(AbstractUser):
    username = models.CharField(max_length=50,unique=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    has_profile = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.username

# client information
class ClientInformation(models.Model):
    user = models.OneToOneField(UserCredentials, on_delete=models.CASCADE,null=True)
    
    fullname = models.CharField(max_length=50)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    States = (('AL','AL'),
				  ('AK','AK'),
				  ('AZ','AZ'),
			      ('AR','AR'),
				  ('CA','CA'),
				  ('CO','CO'),
				  ('CT','CT'),
				  ('DE','DE'),
				  ('DC','DC'),
				  ('FL','FL'),
				  ('GA','GA'),
				  ('HI','HI'),
				  ('ID','ID'),
				  ('IL','IL'),
			      ('IN','IN'),
				  ('IA','IA'),
				  ('KY','KY'),
				  ('LA','LA'),
				  ('ME','ME'),
				  ('MD','MD'),
				  ('MA','MA'),
				  ('MI','MI'),
			      ('MN','MN'),
				  ('MS','MS'),
				  ('MO','MO'),
				  ('MT','MT'),
				  ('NE','NE'),
				  ('NV','NV'),
				  ('NH','NH'),
				  ('NJ','NJ'),
				  ('NM','NM'),
				  ('NY','NY'),
				  ('ND','ND'),
				  ('OH','OH'),
				  ('OK','OK'),
				  ('OR','OR'),
				  ('PA','PA'),
				  ('RI','RI'),
				  ('SD','SD'),
				  ('TN','TN'),
				  ('TX','TX'),
				  ('UT','UT'),
				  ('VT','VT'),
			 	  ('VA','VA'),
			      ('WA','WA'),
				  ('WV','WV'),
				  ('WI','WI'),
				  ('WY','WY')
                 )
                 
    state = models.CharField(choices = States, max_length=2, null = False)
    
    
    zipcode = models.CharField(max_length=9,validators=[RegexValidator(regex=r'^(^[0-9]{5}(?:-[0-9]{4})?$|^$)')])

    @receiver(post_save,sender=UserCredentials)
    def create_user_profile(sender,instance, created, **kwards):
        if (created):
            ClientInformation.objects.create(user=instance)
            
    def save_user_profile(sender,instance, **kwards):
        instance.profile.save()
#fuel quote model
class Fuel_Quote(models.Model):
    username = models.CharField(null = True, max_length=50,unique=False)
    
    gallons_requested = models.PositiveIntegerField(default = 1, validators=[MinValueValidator(1)],null = True)
    delivery_address = models.CharField(max_length=100,null = True)
    delivery_date = models.DateField(null=True)
    suggested_price = models.PositiveIntegerField(default = 0, validators=[MinValueValidator(0)],null = True)
    total_due = models.PositiveIntegerField(default = 0, validators=[MinValueValidator(0)],null = True)
