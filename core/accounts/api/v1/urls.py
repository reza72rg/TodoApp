from django.urls import path
#from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterApiViews, CustomAuthToken, CustomDiscardAuthToken, \
    CustomTokenObtainPairView, ChangePasswordApiView, ProfileApiViews
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


app_name = 'api-v1'

urlpatterns = [
    # Registration
    path("register/", RegisterApiViews.as_view(), name="register"),
    
    # Change Password
    path("change-password",ChangePasswordApiView.as_view(),name="change-password"),
    
    # Login Token 
    #path('token/login', obtain_auth_token,name="token-login"),
    path('token-custom/login/', CustomAuthToken.as_view(),name="token-login"),
    path('token/logout/', CustomDiscardAuthToken.as_view(),name="token-logout"),
    
    # Login JWT
    path('jwt/create/', CustomTokenObtainPairView.as_view(), name='jwt-create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='jwt-verify'),
    
    # Profile
    path('profile/', ProfileApiViews.as_view(), name='profile'),
    
]