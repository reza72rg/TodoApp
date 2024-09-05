from django import forms
from todo.models import Task


# Task form for creating new tasks
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("title", "description", "status")
