from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = [
            "username", "password", "confirm_password", "email", "name", 
            "nickname", "date_of_birth", "gender", "subscription"
        ]
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def validate(self, data):
        password = data.get("password")
        username = data.get("username")
        confirm_password = data.pop("confirm_password", None)
        
        if username == password:
            raise serializers.ValidationError("아이디와 비밀번호를 다르게 입력해주세요.")
        if not password:
            raise serializers.ValidationError("비밀번호를 입력해주세요.")
        if password != confirm_password:
            raise serializers.ValidationError("비밀번호가 서로 일치하지 않습니다.")
        validate_password(password)
        return data