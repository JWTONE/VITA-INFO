from rest_framework import serializers
from Survey.models import SurveyInfo, SurveyResults

class SurveySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SurveyInfo
        exclude = ["user"]

class SurveyResultsSerializer(serializers.ModelSerializer):

    class Meta:
        model = SurveyResults
        exclude = ["survey_id"]
