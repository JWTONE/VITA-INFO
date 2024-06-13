from django.urls import path
from .views import SurveyAPIView
from . import views

app_name = "survey"

urlpatterns = [
    path("", SurveyAPIView.as_view(), name="survey"),
    path("loading/", views.loading, name='loading'),
    path("result/", views.loading, name='result'),
    path("result/<int:user_pk>/", views.results, name='result'),
]
