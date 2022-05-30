# HttpResponse는 "안녕하세요! 장고의 시작입니다!"를 전달하는 역할을 한다
from django.http import HttpResponse
# render는 html파일을 보여주는 역할을 한다
from django.shortcuts import render

def base_response(request):
    return HttpResponse("안녕하세요! 장고의 시작입니다!")

# first_view 함수는 my_test.html을 보여준다
# 함수를 만들었으니 url과 연동시켜 주어야 한다.
def first_view(request):
    return render(request, 'my_test.html')