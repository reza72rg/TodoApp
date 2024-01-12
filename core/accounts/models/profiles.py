from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .users import User


# Profile Model
class Profile(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # Foreign key relation with User model
    first_name = models.CharField(max_length=250)  # First name of the user
    last_name = models.CharField(max_length=250)  # Last name of the user
    image = models.ImageField(
        blank=True, null=True
    )  # Image field for user profile picture
    descriptions = (
        models.TextField()
    )  # Text field for user profile description
    create_date = models.DateTimeField(
        auto_now_add=True
    )  # Date and time when profile was created
    update_date = models.DateTimeField(
        auto_now=True
    )  # Date and time when profile was last updated

    def __str__(self):
        return self.user.email


# Signal to create profile when user is created
@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
