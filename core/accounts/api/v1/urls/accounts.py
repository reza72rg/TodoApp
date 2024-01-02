from django.urls import path
#from rest_framework.authtoken.views import obtain_auth_token
from ..views import RegisterApiViews, CustomAuthToken, CustomDiscardAuthToken, \
    CustomTokenObtainPairView, ChangePasswordApiView, SendEmail
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)



urlpatterns = [
    # Registration
    path("register/", RegisterApiViews.as_view(), name="register"),
    
    # Verify
    path('send-email',SendEmail.as_view(),name="send-email"),
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
    
]