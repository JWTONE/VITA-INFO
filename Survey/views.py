from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from Survey.serializers import SurveySerializer
from rest_framework.permissions import IsAuthenticated


class SurveyAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        print(user.username)
        serializer = SurveySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)