from django.shortcuts import render, redirect
# .은 내가 가지고 있는 위치 나의 위치와 동일한 친구중에 models을 갖고 올 건데 라는 의미
# 그 우리의 models.py 중에서 UserModel 이라는 친구를 가져온다
from .models import UserModel
# 화면에 글자 띄우는 역할
from django.http import HttpResponse
# 사용자가 db 안에 있는지 검사하는 함수이다
from django.contrib.auth import get_user_model
# 사용자 auth 기능
from django.contrib import auth
# @login_required 하면 그 아래의 함수는 로그인을 해야만 접근 가능한 함수가 된다
from django.contrib.auth.decorators import login_required




# Create your views here.
def sign_up_view(request):
    # sign_up_view에 요청이 들어오는 url 실행할 때 .method 를 확인하게 된다
    if request.method == 'GET':
        # request.user.is_authenticated 이 코드로 유저가 로그인/인증 되어있는지 한번에 확인한다
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return redirect('user/signup.html')

        # return render(화면을 보여준다) user/signup.html 화면을 보여주겠다.
        return render(request, 'user/signup.html')
    elif request.method == 'POST':
        # post로 온 데이터를 이렇게 받는다 그리고 받은것 중에서 input 태그 안에 username이라는
        # 이름으로 되었는 데이터를 가져오고 싶다 만약 username이 없다면 none 빈칸 처리하겠다는 의미
        # 마지막으로 그 데이터를 username이라는 변수에 저장한다
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        bio = request.POST.get('bio', None)

        # != 같지 않다면
        if password != password2:
            # 저장 되면 안 되니까 다시 한번 해당 화면 보여준다.
            return render(request, 'user/signup.html')
        else:
            # get_user_model() 함수(사용자가 db에 있는지 검사하는 함수)
            # 사용해 db에 username을 가진 사람이 있는지 확인한다
            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, 'user/signup.html')  # 사용자가 존재하기 때문에 사용자를 저장하지 않고 회원가입 페이지를 다시 띄움
            else:
                # 장고의 기능! create_user() 함수를 사용해 username, password, bio를 db에 저장한다
                UserModel.objects.create_user(username=username, password=password, bio=bio)
                return redirect('/sign-in')  # 회원가입이 완료되었으므로 로그인 페이지로 이동

        # ===================5줄의 코드를 한줄로 위에 작성했다=======================
            # # new_user 안에 UserModel()을 넣어준다.
            # new_user = UserModel()
            # # 넣은 UserModel() 안에 username 안에 username을 넣어준다
            # new_user.username = username
            # new_user.password = password
            # new_user.bio = bio
            # # 위에까지는 db에 저장이 안되고
            # # new_user.save()를 작성하므로 db에 저장된다
            # new_user.save()
        #     ==========================================================================

        # 저장 다 되면 회원가입 페이지 말고 로그인 페이지 보여주고 싶어! 이때 redirect 사용(import도 해야함)
        return redirect('/sign-in')



def sign_in_view(request):
    if request.method == 'POST':
        # request.POST안에는 요청한 post 전부가 담겨 있다
        # 우리는 그 중에 username을 가져오는것(input 태그 안의 username)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        # 장고 모듈로 유저 네임 패스워드 넣어주기
        # authenticate() 함수는 암호화된 비밀번호와 현재 입력된 비밀번호가 일치하는지 또 사용자와 맞는지 확인해준다
        # 맞으면 me에 정보가 들어간다
        me = auth.authenticate(request, username=username, password=password)
        # 사용자가 있는지 없는지 확인만 해주면 된다 위의 코드가 모든 사용자의 정보를 체크해주기 때문이다
        # 사용자가 있다면
        if me is not None:
            # 장고가 알아서 정보를 넣어준다./////?????
            auth.login(request, me)

    # ========================아래의 코드는 비번 암호화하면 로그인 못한다==========================
        # # UserModel은 이미 db와 연결되있는 class이다 objects에서 가져오는데
        # # 왼쪽의 username은 우리가 넣은 username이 아니라 UserModel안에 있던 username이다.
        # # db usernamee과 우리가 post에서 받아온 username 데이터와 같은 친구를 부른다!!
        # # 그러면 회원가입된 사람만 불러올 수 있다(db안에 있어야 하니까)
        # me = UserModel.objects.get(username=username)
    # ======================================================================================
    # ==========================이 코드도 장고가 간단하게 해 준다=================================
    #     # 불러온 me의(db) 비번과 post에서 가져온 비번이 같다면
    #     if me.password == password:
    #         # 같으면 로그인해도 되니까 세션에(사용자 정보 저장하는 공간) user을 넣어준다
    #         request.session['user'] = me.username
    # ======================================================================================

            return redirect('/')
        else:
            return redirect('/sign-in')

    elif request.method == 'GET':
        # request.user.is_authenticated 이 코드로 유저가 로그인/인증 되어있는지 한번에 확인한다
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/signin.html')

# login_required 는 사용자가 로그인 해야만 접근이 가능한 함수라는 것을 말해주는것이다
@login_required
def logout(request):
    # 장고 사용 안하면 request에 사용자 있는지 여부 세션에서 확인하고 등등의 여러 작업을 해 주어야 한다
    auth.logout(request)
    return redirect('/')