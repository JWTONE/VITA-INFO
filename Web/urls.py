from django.urls import path
from . import views


app_name = "web"

urlpatterns = [
    path("login/", views.login, name="login"),
    # #user
    # path("signup/", views.signup, name="signup"),
    # path("update/", views.update, name="update"),
    
    # # #post
    # path("create/", views.create, name="create"),

    # #survey
    path("surveymain/", views.surveymain, name="surveymain"),
    path("surveyresult/", views.surveyresult, name="surveyresult"),
    
]