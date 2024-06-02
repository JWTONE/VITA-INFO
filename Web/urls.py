from django.urls import path
from . import views


app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("post/info/", views.info_list, name ="info_list"),
    path("post/<int:post_pk>/", views.info_detail, name="info_detail"),
    path("mypage/<str:username>/", views.mypage, name="mypage"),

    # #user
    # path("signup/", views.signup, name="signup"),
    path("update/", views.update, name="update"),
    
    # # #post
    # path("create/", views.create, name="create"),

    # #survey
    path("surveymain/", views.surveymain, name="surveymain"),
    path("surveyresult/", views.surveyresult, name="surveyresult"),
    
]