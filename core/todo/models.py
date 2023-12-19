from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    # ForeignKey relationship with User model
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    # Title field for the task
    title = models.CharField(max_length=200)
    description = models.TextField()
    # Status field to indicate if the task is complete or not
    status =  models.ForeignKey('Status',on_delete=models.SET_NULL,null=True, blank=True)
    
    # Created date field to store the date and time of task creation
    created_date = models.DateTimeField(auto_now_add=True)
    
    # Updated date field to store the date and time of task update
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        # Specify the order of tasks with respect to the user
        order_with_respect_to = "user"
        
        
class Status(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name