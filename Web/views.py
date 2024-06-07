from django.shortcuts import render, redirect
from Survey.forms import SurveyForm
from Account.forms import CustomUserChangeForm, CustomUserPasswordChangeForm, CustomUserCreationForm
from django.shortcuts import get_object_or_404, render
from Post.forms import PostForm
from Post.models import Post
from Post.serializers import PostSerializer
from django.contrib.auth import get_user_model
from Account.serializers import UserCreateSerializer
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.password_validation import validate_password

def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, 'Account/login.html')

def post_list(request, category):
    context = {
        'category': category,
        'form' : PostForm
    }
    if category == "info":
        return render(request, "Post/info_list.html", context) 
    return render(request, "Post/review_list.html", context)


def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            serializer = PostSerializer(data=form.cleaned_data)
            if serializer.is_valid():
                serializer.save(author=request.user)
                return redirect()
            else:
                return Response(status, status=status.HTTP_400_BAD_REQUEST)
    else:
        form = PostForm()
    context = {"form": form}
    return render(request, "Post/post_create.html", context)


def post_detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    context = {
        'post_pk' : post_pk
    }
    if post.category == 'review':
        return render (request, 'Post/review_detail.html', context)
    return render (request, 'Post/info_detail.html', context)

def post_update(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == "GET":
        form = PostForm(instance=post)
    elif request.method =='POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('web:post_detail', post_pk=post_pk)
    context = {
        'form':form,
        'post_pk':post_pk
    }
    return render(request, 'Post/post_edit.html', context)

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
    return render(request, "Account/mypage.html", {"username" : username})

def update(request, username):
    User = get_user_model()
    user = User.objects.get(username=username)
    if request.method == 'GET':
        form = CustomUserChangeForm(instance=user)
    elif request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('web:mypage', username=username)
    context = {
        'form':form,
        'username':username
    }
    return render(request, 'Account/update.html', context)

def password_update(request, username):
    User = get_user_model()
    user = User.objects.get(username=username)
    if request.method == 'GET':
        form = CustomUserPasswordChangeForm(instance=user)
    elif request.method == 'POST':
        form = CustomUserPasswordChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('web:mypage', username=username)
        
    context = {
        'form':form,
        'username':username
    }
    return render(request, 'Account/password_update.html', context)

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            serializer = UserCreateSerializer(data=form.cleaned_data)
            if serializer.is_valid():
                serializer.save()
                return redirect("web:index")
            else:
                return Response(status, status=status.HTTP_400_BAD_REQUEST)
    else:
        form = CustomUserCreationForm()
    context = {"form": form}
    return render(request, "Account/signup.html", context)

def search(request):
    q = request.GET['q']
    context = {
        'q' : q
    }
    return render(request, 'Post/search.html', context)