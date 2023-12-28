from django.urls import path
from .views import * 
from rest_framework.authtoken import views
from .views import RegisterApiViews

app_name = 'api-v1'

urlpatterns = [
    path("register/", RegisterApiViews.as_view(), name="register"),
    path('api-token/', views.obtain_auth_token),
]