from django import forms
from todo.models import Task
# Reordering Form and View
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("title",)


class TaskEditForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("title","status")
