from django.urls import path
from .views import UserListAPIView, LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView

app_name = "account"
urlpatterns = [
    path("", UserListAPIView.as_view(), name="user_list"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]