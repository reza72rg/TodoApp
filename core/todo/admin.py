from django.contrib import admin
from .models import Task

# Register your models here.

# Register the Task model with the admin site
@admin.register(Task)
class PostAdmin(admin.ModelAdmin):
    
    # Specify the fields to be displayed on the change form
    def get_fields(self, request, obj=None):
        return ["title", "status"]
    
    # Specify the fields to be displayed on the change list
    def get_list_display(self, request):
        return ["user", "title", "status"]