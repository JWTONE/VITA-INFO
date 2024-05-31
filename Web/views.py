from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, 'account/login.html')

def info_list(request):
    return render(request, "post/info_list.html")

def info_detail(request, post_pk):
    context = {
        'post_pk' : post_pk
    }
    return render (request, 'post/info_detail.html', context)