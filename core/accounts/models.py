from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from accounts.managers import UserManager
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    #is_verified = models.BooleanField(default=False)
    first_name = models.CharField(max_length=20)
    
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    objects = UserManager()
    
    def __str__(self):
        return self.email

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 250)
    last_name = models.CharField(max_length = 250)
    image = models.ImageField(blank=True,null=True)
    descriptions = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.email



@receiver(post_save, sender=User)
def save_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user= instance)
