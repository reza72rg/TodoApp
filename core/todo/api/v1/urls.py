from django.urls import path
from .views import TaskListViewSet, StatusListModuleSet, UsersListModuleSet
from rest_framework.routers import DefaultRouter

app_name = "api-v1"

'''router = DefaultRouter()
router.register("task", TaskListViewSet, basename="task")
router.register("status", StatusListModuleSet, basename="status")
router.register("users", UsersListModuleSet, basename="users")
urlpatterns = router.urls'''
urlpatterns = [
    path(
        "task/",
        TaskListViewSet.as_view({"get": "list", "post": "create"}),
        name="task-list",
    ),
    path(
        "status/",
        StatusListModuleSet.as_view({"get": "list", "post": "create"}),
        name="status-list",
    ),
    path(
        "task/<int:pk>/",
        TaskListViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="task-detail",
    ),
    path(
        "status/<int:pk>/",
        StatusListModuleSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="status-detail",
    ),
]

