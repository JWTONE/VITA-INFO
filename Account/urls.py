from django.urls import path
from .views import UserListAPIView, LogoutView, PasswordUpdateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from . import views

app_name = "account"
urlpatterns = [
    path("", UserListAPIView.as_view(), name="user_list"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("<str:username>/", UserListAPIView.as_view(), name="profile_update"),
    path("<str:username>/password/",
         PasswordUpdateAPIView.as_view(), name="password_update")
]
