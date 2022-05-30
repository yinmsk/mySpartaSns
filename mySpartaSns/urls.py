"""mySpartaSns URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# 지금 내가 있는 폴더에서 views라는 파일을 가져온다는 뜻이다
from. import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # test라는 url로 views의 base_response라는 함수와 연결한다는 뜻이다
    # http://127.0.0.1:8000/test/ 로 접속 가능! 접속하면 "안녕하세요! 장고의 시작입니다!" 가 나온다
    path('test/', views.base_response, name='first_test'),
    # 위의 것과 비슷한 의미 다른 점은
    # html에 "테스트 페이지 입니다! 장고를 사용했어요!"라는 글이 있고
    # 그 html과 views.py의 first_view() 함수가 import render로 연결되 있고
    # 그 연결된 함수를 지금의 urls.py에서 url주소를 통해 우리가 볼 수 있게 된거다
    # http://127.0.0.1:8000/first 로 접속 가능! 접속하면 "테스트 페이지 입니다! 장고를 사용했어요!" 가 나온다
    path('first/', views.first_view, name='first_view'),
    # include를 사용해 user안에 있는 urls.py와 연결했다
    path('',include('user.urls')),
    path('', include('tweet.urls'))
]
