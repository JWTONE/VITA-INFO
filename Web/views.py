from django.shortcuts import render
from Survey.forms import SurveyForm

def login(request):
    return render(request, 'account/login.html')


def surveymain(request):
    context = {'form':SurveyForm}
    return render(request, 'Survey/survey.html', context)

def surveyresult(request):
    context = {'form':SurveyForm}
    return render(request, 'Survey/survey_result.html', context)