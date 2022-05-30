from django.shortcuts import render, redirect
# 글쓰기 모델 가져오기
from .models import TweetModel
from django.contrib.auth.decorators import login_required

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
    if request.method == 'GET':  # 요청하는 방식이 GET 방식인지 확인하기
        user = request.user.is_authenticated  # 사용자가 로그인이 되어 있는지 확인하기
        if user:  # 로그인 한 사용자라면
            # TweetModel.objects.all() 는 TweetModel의 모든 데이터를 불러와라 라는 뜻이다
            # order_by('-created_at') 는 tweet이 생성된 시간을 역순으로 출력해준다 ()안에 -는 역순 정렬을 위해 사용했다
            all_tweet = TweetModel.objects.all().order_by('-created_at')
            # 딕셔너리 형태로 데이터를 불러올 수 있도록 했다
            return render(request, 'tweet/home.html', {'tweet': all_tweet})
        else:  # 로그인이 되어 있지 않다면
            return redirect('/sign-in')
    elif request.method == 'POST':  # 요청 방식이 POST 일때
        user = request.user  # 현재 로그인 한 사용자를 불러오기
        my_tweet = TweetModel()  # 글쓰기 모델 가져오기
        my_tweet.author = user  # 모델에 사용자 저장
        my_tweet.content = request.POST.get('my-content', '')  # 모델에 글 저장
        my_tweet.save()
        return redirect('/tweet')


@login_required
def delete_tweet(request, id):
    my_tweet = TweetModel.objects.get(id=id)
    my_tweet.delete()
    return redirect('/tweet')


# def write_comment():
#
#
# def delete_comment():