from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    # 유저가 있는지 판단하기 위해 user 변수를 만든다
    # request.user.is_authenticated 이 코드로 유저가 로그인/인증 되어있는지 한번에 확인한다
    user = request.user.is_authenticated
    if user:
        return redirect('/tweet')
    else:
        return redirect('/sign-in')

# tweet 안의 home.html을 보여주는 함수
def tweet(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            # render(html 보여주는 함수) tweet 안의 home.html을 보여준다
            return render(request, 'tweet/home.html')
        else:
            return redirect('sign-in')




