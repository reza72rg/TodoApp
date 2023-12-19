from django.contrib import admin
from .models import Task,Status

# Register your models here.

# Register the Task model with the admin site
@admin.register(Task)
class PostAdmin(admin.ModelAdmin):
    
    # Specify the fields to be displayed on the change form
    def get_fields(self, request, obj=None):
        return ["user", "title", "description","status"]
    
    # Specify the fields to be displayed on the change list
    def get_list_display(self, request):
        return ["user", "title", "description","status"]
    
@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    
    # Specify the fields to be displayed on the change form
    def get_fields(self, request, obj=None):
        return ["name"]
    
    # Specify the fields to be displayed on the change list
    def get_list_display(self, request):
        return ["name"]