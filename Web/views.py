from django.shortcuts import render
from Survey.forms import SurveyForm

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


def surveymain(request):
    context = {'form':SurveyForm}
    return render(request, 'Survey/survey.html', context)

def surveyresult(request):
    context = {'form':SurveyForm}
    return render(request, 'Survey/survey_result.html', context)

def mypage(request, username):
    return render(request, "account/mypage.html", {"username" : username})

def update(request):
    pass
# def update(request):
#     try:
#         data = json.loads(request.body)
#         form = CustomUserChangeForm(data, instance=request.user)
        
#         if form.is_valid():
#             form.save()
#             return redirect("account:mypage")  # 마이페이지로 리다이렉트
#         else:
#             # 유효성 검사에 실패한 경우에 대한 처리
#             # 예를 들어, 유효성 검사 오류 메시지를 함께 전달하거나 다시 입력 폼을 표시할 수 있습니다.
#             return render(request, "account/update_failed.html", {"form": form})
#     except JSONDecodeError:
#         # 요청의 본문이 유효한 JSON 형식이 아닌 경우에 대한 처리
#         # 예를 들어, 오류 메시지를 반환하거나 다시 시도하도록 유도할 수 있습니다.
#         return HttpResponse("Invalid JSON data", status=400)