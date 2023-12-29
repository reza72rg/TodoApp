from django.urls import path
#from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterApiViews, CustomAuthToken, CustomDiscardAuthToken

app_name = 'api-v1'

urlpatterns = [
    path("register/", RegisterApiViews.as_view(), name="register"),
    #path('token/login', obtain_auth_token,name="token-login"),
    path('token-custom/login', CustomAuthToken.as_view(),name="token-login"),
    path('token/logout', CustomDiscardAuthToken.as_view(),name="token-logout"),
]