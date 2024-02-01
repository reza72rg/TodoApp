from django.urls import path, include
from .views import CustomLoginView, RegisterPage, send_email, test
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
    path("api/v1/", include("accounts.api.v1.urls")),
    path("api/v2/", include("djoser.urls")),
    path("api/v2/", include("djoser.urls.jwt")),
    path("send-email/", send_email, name="send_email"),
    path("test/", test, name="test"),
    
]
