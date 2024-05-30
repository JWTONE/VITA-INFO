from django import forms
from .models import SurveyInfo

class SurveyForm(forms.ModelForm):
    class Meta:
        model = SurveyInfo

    
        exclude = ["user"]
    