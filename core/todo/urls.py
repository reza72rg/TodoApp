from django.urls import path
from todo.views import *

# Set the app name for namespacing
app_name = 'todo'

urlpatterns = [
    # Task list view
    path("", Tasklist.as_view(), name="task_list"),

    # Task create view
    path("create/", TaskCreate.as_view(), name="create_task"),

    # Task delete view
    path("delete/<int:pk>/", DeleteView.as_view(), name="delete_task"),

    # Task done view
    path("done/<int:pk>/", TaskDone.as_view(), name="done_task"),
    
    # Task update view
    path("edit/<int:pk>/", TaskUpdate.as_view(), name="update_task"),
]