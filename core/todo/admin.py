from django.contrib import admin

# Register your models here.
from .models import Task

@admin.register(Task)
class PostAdmin(admin.ModelAdmin):

    def get_fields(self, request, obj=None):
        return ["title","status"]

    def get_list_display(self, request):
        return [ "user","title",  "status"]