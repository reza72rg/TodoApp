from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from accounts.models.managers import UserManager



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

