#user/models.py
from django.db import models
#
from django.contrib.auth.models import AbstractUser


# Create your models here.
# 장고에서 제공하는 기본적인 유저 모델을 사용하겠다.(상속한다. (auth_user 테이블과 연동되는 클래스: AbstractUser))
# 장고 기본 모델 플러스 bio라는 다른 정보도 넣는다
class UserModel(AbstractUser):
    class Meta:
        # db_table의 이름은 my_user
        db_table = "my_user"

    bio = models.CharField(max_length=256, default='')
