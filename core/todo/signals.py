from django.core.cache import cache
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from .models import Task


@receiver(post_delete, sender=Task, dispatch_uid="post_deleted")
def object_post_delete_handler(sender, instance, **kwargs):
    cache.clear()


@receiver(post_save, sender=Task, dispatch_uid="posts_updated")
def object_post_save_handler(sender, instance, **kwargs):
    cache.clear()
