# 장고에서 admin툴을 사용하겠다
from django.contrib import admin
# 우리의 위치와 동일하게 있는 modles라는 파이썬 파일을 불러오겠다
# 그 중에 UserModel이라는 모델을 가져오겠다
# models.py에 "class UserModel(models.Model):" 라는 모델이 있는데 이거 가져옴
from .models import UserModel

# Register your models here.
admin.site.register(UserModel) # 이 코드가 나의 UserModel을 Admin에 추가 해 줍니다