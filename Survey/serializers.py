from rest_framework import serializers
from Survey.models import SurveyInfo

class SurveySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SurveyInfo
        exclude = ['user']

