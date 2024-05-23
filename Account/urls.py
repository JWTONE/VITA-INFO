from django.urls import path
from .views import UserListAPIView

app_name = "account"
urlpatterns = [
    path("", UserListAPIView.as_view(), name="user_list"),
]