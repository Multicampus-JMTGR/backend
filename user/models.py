from django.db import models

# 사용자 테이블
class User(models.Model):
    id_token = models.CharField(primary_key=True, max_length=500) #PK(사용자PK / Auth에서 제공하는 id)
    secret_key = models.CharField(max_length=500) #비밀키(이걸 저장하는게 맞는진 잘 모르겠음...)
    interest = models.CharField(max_length=50) #관심영역(회원가입 시 선택)
    name = models.CharField(max_length=50) #사용자 이름
    email = models.CharField(max_length=50) #사용자 이메일
    phone_number = models.CharField(max_length=50) #핸드폰 번호

    class Meta:
        db_table = 'USER'
    
    def __str__(self):
        return self.name