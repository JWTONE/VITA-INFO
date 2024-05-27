import json
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from Survey.serializers import SurveySerializer
from rest_framework.permissions import IsAuthenticated
from .function import survey

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
                result_json = {'error': 'Invalid result format'}
            serializer.save(user=user)
            response_data = {
                'survey': serializer.data,
                'result': result_json
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        