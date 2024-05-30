from django.urls import path
from .views import SurveyAPIView
from . import views

app_name = "survey"

urlpatterns = [
    #WV
    path("surveymain/", views.survey_view, name="surveymain"),
    
    #API
    path("", SurveyAPIView.as_view(), name="survey"),
    
]