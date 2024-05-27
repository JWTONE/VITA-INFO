from ast import literal_eval
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from Survey.serializers import SurveySerializer, SurveyResultsSerializer
from rest_framework.permissions import IsAuthenticated
from .function import survey

class SurveyAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        serializer = SurveySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            query = serializer.validated_data
            result = literal_eval(survey(query))
            survey_result = serializer.save(user=user)

            # SurveyResults 모델에 데이터를 저장
            survey_results_data = {
                'recommended_nutrients_1': result["recommended_nutrients"]["1"],
                'recommended_nutrients_2': result["recommended_nutrients"]["2"],
                'recommended_nutrients_3': result["recommended_nutrients"]["3"],
                'synergistic_nutrients_1': result["synergistic_nutrients"]["1"],
                'synergistic_nutrients_2': result["synergistic_nutrients"]["2"],
                'synergistic_nutrients_3': result["synergistic_nutrients"]["3"],
                'antagonistic_nutrients_1': result["antagonistic_nutrients"]["1"],
                'antagonistic_nutrients_2': result["antagonistic_nutrients"]["2"],
                'antagonistic_nutrients_3': result["antagonistic_nutrients"]["3"],
                'alternative_foods_1': result["alternative_foods"]["1"],
                'alternative_foods_2': result["alternative_foods"]["2"],
                'alternative_foods_3': result["alternative_foods"]["3"],
                'incompatible_foods_1': result["incompatible_foods"]["1"],
                'incompatible_foods_2': result["incompatible_foods"]["2"],
                'incompatible_foods_3': result["incompatible_foods"]["3"],
            }
            survey_results_serializer = SurveyResultsSerializer(data=survey_results_data)
            if survey_results_serializer.is_valid(raise_exception=True):
                survey_results_serializer.save(survey_id = survey_result)

            response_data = {
                "survey": serializer.data,
                "result": survey_results_serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)