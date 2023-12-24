from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin site URL
    path('admin/', admin.site.urls),
    
    # URLs for the accounts app
    path('accounts/', include('accounts.urls')),
    path('api-auth/', include('rest_framework.urls')),
    # path("accounts/", include("django.contrib.auth.urls")),
    # URLs for the todo app
    path("", include("todo.urls")),
]