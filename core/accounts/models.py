from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from accounts.managers import UserManager
from django.db.models.signals import post_save
from django.dispatch import receiver

# Custom User Model
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)  # Email field for user authentication
    is_staff = models.BooleanField(default=False)  # Boolean field to indicate if user is staff or not
    is_active = models.BooleanField(default=True)  # Boolean field to indicate if user is active or not
    first_name = models.CharField(max_length=20)  # First name of the user
    
    REQUIRED_FIELDS = []  # Required fields for user registration
    USERNAME_FIELD = 'email'  # Field to use for user authentication
    
    create_date = models.DateTimeField(auto_now_add=True)  # Date and time when user was created
    update_date = models.DateTimeField(auto_now=True)  # Date and time when user was last updated
    
    objects = UserManager()  # Manager for user model
    
    def __str__(self):
        return self.email

# Profile Model
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Foreign key relation with User model
    first_name = models.CharField(max_length=250)  # First name of the user
    last_name = models.CharField(max_length=250)  # Last name of the user
    image = models.ImageField(blank=True, null=True)  # Image field for user profile picture
    descriptions = models.TextField()  # Text field for user profile description
    create_date = models.DateTimeField(auto_now_add=True)  # Date and time when profile was created
    update_date = models.DateTimeField(auto_now=True)  # Date and time when profile was last updated
    
    def __str__(self):
        return self.user.email

# Signal to create profile when user is created
@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)