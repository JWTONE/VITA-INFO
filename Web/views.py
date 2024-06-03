from django.shortcuts import render
from Survey.forms import SurveyForm
from Account.forms import CustomUserChangeForm
from django.contrib.auth import get_user_model

def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, 'account/login.html')


def post_list(request, category):
    context = {
        'category': category
    }
    if category == "info":
        return render(request, "post/info_list.html", context) 
    return render(request, "post/review_list.html", context)

def post_detail(request, post_pk):
    context = {
        'post_pk' : post_pk
    }
    return render (request, 'post/info_detail.html', context)

def review_list(request):
    return render(request, "post/user_list.html")

def review_detail(request, post_pk):
    context = {
        'post_pk' : post_pk
    }
    return render (request, 'post/review_detail.html', context)

def surveymain(request):
    context = {'form':SurveyForm}
    return render(request, 'Survey/survey.html', context)

def surveyloading(request):
    context = {'form':SurveyForm}
    return render(request, 'Survey/survey_loading.html', context)

def surveyresult(request):
    context = {'form':SurveyForm}
    return render(request, 'Survey/survey_result.html', context)

def mypage(request, username):
    return render(request, "account/mypage.html", {"username" : username})

def update(request, username):
    User = get_user_model()
    user = User.objects.get(username=username)
    if request.method == 'GET':
        form = CustomUserChangeForm(instance=user)
    elif request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        
    context = {
        'form':form,
        'username':username
    }
    return render(request, 'account/update.html', context)