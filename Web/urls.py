from django.urls import path
from . import views


app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("post/create/", views.post_create, name="post_create"),
    path("post/<int:post_pk>/", views.post_detail, name="post_detail"),
    path("post/<str:category>/", views.post_list, name ="post_list"),
    path("mypage/<str:username>/", views.mypage, name="mypage"),

    # #user
    # path("signup/", views.signup, name="signup"),
    path("update/<str:username>", views.update, name="update"),
    
    # # #post
    # path("create/", views.create, name="create"),

    # #survey
    path("surveymain/", views.surveymain, name="surveymain"),
    path("surveyloading/", views.surveyloading, name="surveyload"),
    path("surveyresult/", views.surveyresult, name="surveyresult"),
    
]