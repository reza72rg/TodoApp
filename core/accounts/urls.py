from django.urls import path
from .views import CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

# Set the app name for namespacing
app_name = "accounts"

urlpatterns = [
    # Login view
    path("login/", CustomLoginView.as_view(), name="login"),
    
    # Logout view
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
    
    # Register view
    path("register/", RegisterPage.as_view(), name="register"),
]