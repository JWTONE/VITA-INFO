from django.urls import path
from .views import SurveyAPIView
app_name = "survey"

urlpatterns = [
    path("", SurveyAPIView.as_view(), name="survey")
]