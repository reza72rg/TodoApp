from django.urls import path
from todo.views import *
app_name = 'todo'

urlpatterns = [
    path("", Tasklist.as_view(), name="task_list"),
    path("create/", TaskCreate.as_view(), name="create_task"),
    path("delete/<int:pk>/", DeleteView.as_view(), name="delete_task"),
    path("done/<int:pk>/", TaskComplete.as_view(), name="complete_task"),
    path("edit/<int:pk>/", TaskUpdate.as_view(), name="update_task"),
]
