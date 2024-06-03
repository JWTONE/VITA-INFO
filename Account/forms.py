from .models import User
from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label="비밀번호",
        required=True,
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(),
        label="비밀번호 확인",
        required=True,
    )
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="생년월일"
    )

    class Meta:
        model = User
        fields = [
            "username", "password", "confirm_password", "email", "name",
            "nickname", "date_of_birth", "gender", "subscription"
        ]
        labels = {
            "username": "아이디",
            "password": "비밀번호",
            "email": "이메일",
            "name": "이름",
            "nickname": "닉네임",
            "gender": "성별",
            "subscription": "구독 여부"
        }
        help_texts = {
            'username': '',
            'password': '',
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password", "비밀번호가 일치하지 않습니다.")

class CustomUserChangeForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="생년월일",
        required=False,
    )

    class Meta:
        model = User
        fields = [
            "email", "name",
            "nickname", "date_of_birth", "gender", "subscription"
        ]
        labels = {
            "email": "이메일",
            "name": "이름",
            "nickname": "닉네임",
            "gender": "성별",
            "subscription": "구독 여부"
        }
        help_texts = {
            'username': '',
        }

class CustomUserPasswordChangeForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label="비밀번호",
        required=True,
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(),
        label="비밀번호 확인",
        required=True,
    )

    class Meta:
        model = User
        fields = [
            "password", "confirm_password"
        ]
        labels = {
            "password": "비밀번호",
        }
        help_texts = {
            'password': '',
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password", "비밀번호가 일치하지 않습니다.")

        try:
            validate_password(password, self.instance)
        except ValidationError as e:
            self.add_error('password', e)