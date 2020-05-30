from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("api/token/", TokenObtainPairView.as_view(), name="token"),
    path("api/register", views.ProfileList.as_view(), name="register")
]
