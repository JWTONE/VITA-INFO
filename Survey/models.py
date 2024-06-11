from django.db import models
from Account.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class SurveyInfo(models.Model):
    GENDER_CHOICES = [
        ("남자", "남자"),
        ("여자", "여자"),
    ]
    EXERCISE_CHOICES = [
        ("0", "주0회"),
        ("1", "주1회"),
        ("2~3", "주2~3회"),
        ("4이상", "주4회 이상"),
    ]
    SLEEP_CHOICES = [
        ("5~8", "5~8시간"),
        ("8~10", "8~10시간"),
        ("10~12", "10~12시간"),
        ("12이상", "12시간 이상"),
    ]
    EAT_CHOICES = [
        ("1", "1회"),
        ("2", "2회"),
        ("3", "3회"),
        ("4이상", "4회 이상"),
    ]
    SMOKE_CHOICES = [
        ("예", "예"),
        ("아니오", "아니오"),
    ]
    DIET_CHOICES = [
        ("고기 위주", "고기 위주"),
        ("채식 위주", "채식 위주"),
        ("균형잡힌 식단", "균형잡힌 식단"),
    ]
    SNACK_CHOICES = [
        ("과일", "과일 위주"),
        ("견과류", "견과류 위주"),
        ("패스트푸드", "패스트푸드"),
        ("과자", "디저트 위주"),
        ("OTHER", "기타"),
    ]
    HEALTHGOAL_CHOICES = [
        ("체중감량", "체중감량"),
        ("근육증가", "근육증가"),
        ("면역력 강화", "면역력 강화"),
        ("피부 건강", "피부 건강"),
        ("에너지 증진", "에너지 증진"),
        ("OTHER", "기타"),
    ]
    INTERESTED_CHOICES = [
        ("비타민", "비타민"),
        ("미네랄", "미네랄"),
        ("단백질 보충제", "단백질 보충제"),
        ("오메가 3", "오메가 3"),
        ("OTHER", "기타"),
    ]
    ALCOHOL_CHOICES = [
        ("마시지 않음", "마시지 않음"),
        ("주1~2회", "주1~2회"),
        ("주3회 이상", "주3회 이상"),
    ]
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="survey")
    name = models.CharField(max_length=30)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=20)
    age = models.PositiveIntegerField(validators=[
        MinValueValidator(10),
        MaxValueValidator(120)
    ], max_length=20)
    height = models.PositiveIntegerField(validators=[
        MinValueValidator(50),
        MaxValueValidator(250)
    ])
    weight = models.PositiveIntegerField(validators=[
        MinValueValidator(30),
        MaxValueValidator(290)
    ])
    current_medications_or_supplements = models.TextField()
    allergies = models.TextField()
    exercise_frequency_per_week = models.CharField(
        choices=EXERCISE_CHOICES, max_length=20)
    average_sleep_hours_per_day = models.CharField(
        choices=SLEEP_CHOICES, max_length=20)
    smoking_status = models.CharField(choices=SMOKE_CHOICES, max_length=20)
    alcohol_consumption = models.CharField(
        choices=ALCOHOL_CHOICES, max_length=20)
    average_meals_per_day = models.CharField(
        choices=EAT_CHOICES, max_length=20)
    main_foods = models.CharField(choices=DIET_CHOICES, max_length=20)
    snacks = models.CharField(choices=SNACK_CHOICES,
                              max_length=100, default="과일")
    snacks_other = models.CharField(max_length=100, blank=True)
    health_goals = models.CharField(
        choices=HEALTHGOAL_CHOICES, max_length=100, default="체중감량")
    health_goals_other = models.CharField(max_length=100, blank=True)
    interested_supplements = models.CharField(
        choices=INTERESTED_CHOICES, max_length=100, default="비타민")
    interested_supplements_other = models.CharField(max_length=100, blank=True)
    specific_health_issues_to_improve = models.TextField(
        max_length=300, blank=True, null=True)


class SurveyResults(models.Model):
    survey_id = models.ForeignKey(
        SurveyInfo, on_delete=models.CASCADE, related_name="survey")
    recommended_nutrients_1 = models.TextField()
    recommended_nutrients_2 = models.TextField()
    recommended_nutrients_3 = models.TextField()
    synergistic_nutrients_1 = models.TextField()
    synergistic_nutrients_2 = models.TextField()
    synergistic_nutrients_3 = models.TextField()
    antagonistic_nutrients_1 = models.TextField()
    antagonistic_nutrients_2 = models.TextField()
    antagonistic_nutrients_3 = models.TextField()
    alternative_foods_1 = models.TextField()
    alternative_foods_2 = models.TextField()
    alternative_foods_3 = models.TextField()
    incompatible_foods_1 = models.TextField()
    incompatible_foods_2 = models.TextField()
    incompatible_foods_3 = models.TextField()


class Know_Vitamins(models.Model):
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
