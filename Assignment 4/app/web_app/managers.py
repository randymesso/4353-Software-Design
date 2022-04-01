from django.contrib.auth.base_user import BaseUserManager
from django.contrib import messages

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password):
        if not username:
            raise ValueError("Need Username")
        
        user = self.model(username=username)
        
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self, username, password):
        user = self.create_user(username=username, password=password)
        user.is_admin= True
        user.save(using=self._db)
        return user
        
        