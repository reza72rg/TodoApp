from django.urls import path
#from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterApiViews, CustomAuthToken, CustomDiscardAuthToken, \
    CustomTokenObtainPairView, ChangePasswordApiView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


app_name = 'api-v1'

urlpatterns = [
    path("register/", RegisterApiViews.as_view(), name="register"),
    path("change-password",ChangePasswordApiView.as_view(),name="change-password"),
    #path('token/login', obtain_auth_token,name="token-login"),
    path('token-custom/login/', CustomAuthToken.as_view(),name="token-login"),
    path('token/logout/', CustomDiscardAuthToken.as_view(),name="token-logout"),
    path('jwt/create/', CustomTokenObtainPairView.as_view(), name='jwt-create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='jwt-verify'),
]