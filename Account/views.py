from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.hashers import check_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from Account.forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User
from .serializers import UserCreateSerializer, UserUpdateSerializer, UserPasswordSerializer, CustomTokenObtainPairSerializer

from Account import serializers

##################
#       API      #
##################

class UserListAPIView(APIView):
    def get_object(self, username):
        return get_object_or_404(User, username=username)

    def get(self, request, username):
        user = self.get_object(username)
        if request.user.username == user.username:
            serializer = UserCreateSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, username):
        user = self.get_object(username)
        if request.user.username == user.username:
            serializer = UserUpdateSerializer(
                user, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        user = self.get_object(request.user.username)
        password = request.data.get("password")
        if check_password(password, user.password):
            user.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class PasswordUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, username):
        user = get_object_or_404(User, username=username)
        serializer = UserPasswordSerializer(
            user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.data:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


##################
#       WV       #
##################




# #회원정보 변경 모듈, front와 아직 미연동 상태
# def update(request):
#     if request.method == "POST":
#         form = CustomUserChangeForm(request.POST)
#         if form.is_valid():
#             serializer = UserUpdateSerializer(data=form.cleaned_data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return redirect("account:update")
#             else:
#                 return Response(status, status=status.HTTP_400_BAD_REQUEST)
#     else:
#         form = CustomUserChangeForm()
#     context = {"form": form}
#     return render(request, "account/update.html", context)