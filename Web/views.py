
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from Survey.forms import SurveyForm
from Post.forms import PostForm
from Post.models import Post
from Account.forms import CustomUserChangeForm
from django.contrib.auth import get_user_model

def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, 'account/login.html')

def post_list(request, category):
    context = {
        'category': category,
        'form' : PostForm
    }
    if category == "info":
        return render(request, "post/info_list.html", context) 
    return render(request, "post/review_list.html", context)

def post_create(request):
    context = {
        'form' : PostForm
    }
    return render(request, 'post/post_create.html', context)


def post_detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    context = {
        'post_pk' : post_pk
    }
    if post.category == 'review':
        return render (request, 'post/review_detail.html', context)
    return render (request, 'post/info_detail.html', context)

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

