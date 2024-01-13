from django.urls import path
from ..views import ProfileApiViews


urlpatterns = [
    # Profile
    path("", ProfileApiViews.as_view(), name="profile"),
]
