from django import forms
from .models import SurveyInfo

class SurveyForm(forms.ModelForm):
    name = forms.CharField(
        label="이름",
    )
    
    age = forms.CharField(
        label="나이",
    )
    
    height = forms.CharField(
        label="키",
    )
    
    weight = forms.CharField(
        label="몸무게",
    )
    
    current_medications_or_supplements = forms.CharField(
        label="현재 복용중인 영양제나 약"
    )
    
    allergies = forms.CharField(
        label="알레르기"
    )
    
    gender = forms.ChoiceField(
        label="성별",
        choices=SurveyInfo.GENDER_CHOICES,
        widget=forms.RadioSelect
    )
    exercise_frequency_per_week = forms.ChoiceField(
        label="주당 운동 빈도",
        choices=SurveyInfo.EXERCISE_CHOICES,
        widget=forms.RadioSelect
    )
    average_sleep_hours_per_day = forms.ChoiceField(
        label="하루 평균 수면 시간",
        choices=SurveyInfo.SLEEP_CHOICES,
        widget=forms.RadioSelect
    )
    smoking_status = forms.ChoiceField(
        label="흡연 여부",
        choices=SurveyInfo.SMOKE_CHOICES,
        widget=forms.RadioSelect
    )
    alcohol_consumption = forms.ChoiceField(
        label="주당 음주 빈도",
        choices=SurveyInfo.ALCOHOL_CHOICES,
        widget=forms.RadioSelect
    )
    average_meals_per_day = forms.ChoiceField(
        label="하루 평균 식사 횟수",
        choices=SurveyInfo.EAT_CHOICES,
        widget=forms.RadioSelect
    )
    main_foods = forms.ChoiceField(
        label="주로 섭취하는 음식",
        choices=SurveyInfo.DIET_CHOICES,
        widget=forms.RadioSelect
    )
    snacks = forms.ChoiceField(
        label="간식",
        choices=SurveyInfo.SNACK_CHOICES,
        widget=forms.RadioSelect
    )
    health_goals = forms.ChoiceField(
        label="건강 목표",
        choices=SurveyInfo.HEALTHGOAL_CHOICES,
        widget=forms.RadioSelect
    )
    interested_supplements = forms.ChoiceField(
        label="관심 있는 보충제",
        choices=SurveyInfo.INTERESTED_CHOICES,
        widget=forms.RadioSelect
    )
    specific_health_issues_to_improve = forms.CharField(
        label="그밖에 특정 건강문제",
        required=False
    )
        
    class Meta:
        model = SurveyInfo
        exclude = ["user"]
        js = ("survey_form.js",)