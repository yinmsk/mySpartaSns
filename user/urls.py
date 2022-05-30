from django.urls import path
from . import views

urlpatterns = [
    # https://...sign-up/을 실행하면 sign_up_view이 실행된다
    path('sign-up/', views.sign_up_view, name='sign-up'),
    path('sign-in/', views.sign_in_view, name='sign-in'),
    path('logout/', views.logout, name='logout'),
]