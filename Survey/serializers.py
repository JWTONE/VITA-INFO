from rest_framework import serializers
from .models import KnowVitamins
from Survey.models import KnowVitamins, SurveyInfo, SurveyResults


class SurveySerializer(serializers.ModelSerializer):

    class Meta:
        model = SurveyInfo
        exclude = ["user"]

    def validate(self, data):
        if data.get('snacks') == 'OTHER' and not data.get('snacks_other'):
            raise serializers.ValidationError({"기타": "기타란에 입력하세요"})
        if data.get('health_goals') == 'OTHER' and not data.get('health_goals_other'):
            raise serializers.ValidationError({"기타": "기타란에 입력하세요"})
        if data.get('interested_supplements') == 'OTHER' and not data.get('interested_supplements_other'):
            raise serializers.ValidationError({"기타": "기타란에 입력하세요"})
        return data


class SurveyResultsSerializer(serializers.ModelSerializer):

    class Meta:
        model = SurveyResults
        exclude = ["survey_id"]


class KnowVitaminsSerializer(serializers.ModelSerializer):
    class Meta:
        model = KnowVitamins
        fields = ['name', 'nickname', 'description']
