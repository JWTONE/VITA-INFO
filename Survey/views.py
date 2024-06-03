import json
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from Post import serializers
from Survey.serializers import SurveySerializer, SurveyResultsSerializer
from rest_framework.permissions import IsAuthenticated
from .function import survey
from .forms import SurveyForm
from .models import Know_Vitamins
from rest_framework.decorators import api_view
from random import randint
from .serializers import KnowVitaminsSerializer



##################
#       API      #
##################

class SurveyAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        serializer = SurveySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            query = serializer.validated_data
            result = survey(query)
            try:
                result_json = json.loads(result)  # result를 JSON 형식으로 변환
            except (TypeError, json.JSONDecodeError):
                return Response({'error': 'Invalid result format'}, status=status.HTTP_400_BAD_REQUEST)

            survey_info = serializer.save(user=user)
            # SurveyResults 모델에 데이터를 저장
            survey_results_data = {
                'recommended_nutrients_1': result_json.get('recommended_nutrients', {}).get('1', ''),
                'recommended_nutrients_2': result_json.get('recommended_nutrients', {}).get('2', ''),
                'recommended_nutrients_3': result_json.get('recommended_nutrients', {}).get('3', ''),
                'synergistic_nutrients_1': result_json.get('synergistic_nutrients', {}).get('1', ''),
                'synergistic_nutrients_2': result_json.get('synergistic_nutrients', {}).get('2', ''),
                'synergistic_nutrients_3': result_json.get('synergistic_nutrients', {}).get('3', ''),
                'antagonistic_nutrients_1': result_json.get('antagonistic_nutrients', {}).get('1', ''),
                'antagonistic_nutrients_2': result_json.get('antagonistic_nutrients', {}).get('2', ''),
                'antagonistic_nutrients_3': result_json.get('antagonistic_nutrients', {}).get('3', ''),
                'alternative_foods_1': result_json.get('alternative_foods', {}).get('1', ''),
                'alternative_foods_2': result_json.get('alternative_foods', {}).get('2', ''),
                'alternative_foods_3': result_json.get('alternative_foods', {}).get('3', ''),
                'incompatible_foods_1': result_json.get('incompatible_foods', {}).get('1', ''),
                'incompatible_foods_2': result_json.get('incompatible_foods', {}).get('2', ''),
                'incompatible_foods_3': result_json.get('incompatible_foods', {}).get('3', ''),
            }
            survey_results_serializer = SurveyResultsSerializer(data=survey_results_data)
            if survey_results_serializer.is_valid(raise_exception=True):
                survey_results_serializer.save(survey_id = survey_info)

            response_data = {
                # "survey": serializer.data,
                "result": survey_results_serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        
        
# ##################
# #       WV       #
# ##################

# def survey_view(request):
#     if request.method == "POST":
#         form = SurveyForm(request.POST)
#         if form.is_valid():
#             serializer = SurveySerializer(data=form.cleaned_data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return redirect("survey:survey")
#             else:
#                 return Response(status, status=status.HTTP_400_BAD_REQUEST)
#     else:
#         form = SurveyForm()
#     context = {"form": form}
#     return render(request, "Survey/survey.html", context)

# DB에 있는 Know_Vitamins 가져오기
@api_view(['GET'])
def loading(request):
    all_content = Know_Vitamins.objects.all()
    random_index = randint(0, len(all_content) - 1)
    random_content = all_content[random_index]
    serializer = KnowVitaminsSerializer(random_content)
    
    return Response(serializer.data)