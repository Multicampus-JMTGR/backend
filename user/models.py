from django.db import models
from certificate.models import Certificate, Category


# 사용자 테이블
class User(models.Model):
    email = models.CharField(primary_key=True, max_length=50)  # 사용자 이메일
    interest = models.CharField(max_length=50)  # 관심영역(회원가입 시 선택 / 카테고리 명)
    name = models.CharField(max_length=50)  # 사용자 이름
    phone_number = models.CharField(max_length=50)  # 핸드폰 번호
    # 좋아요 Many to Many 설정 방법
    cat_likes = models.ManyToManyField(Category, blank=True, db_constraint=True, related_name='cat_likes')
    cert_likes = models.ManyToManyField(Certificate, blank=True, db_constraint=True, related_name='cert_likes')

    class Meta:
        db_table = 'USER'

    def __str__(self):
        return self.name


# 스터디 플랜
# ondelete 설명 : https://lee-seul.github.io/django/backend/2018/01/28/django-model-on-delete.html
class StudyPlan(models.Model):
    content = models.AutoField(primary_key=True)  # PK(스터디플랜PK)
    email = models.ForeignKey(User, on_delete=models.CASCADE, related_name='study_plan')  # FK(사용자PK) 
    cert = models.ForeignKey(Certificate, on_delete=models.CASCADE)  # FK(자격증PK)
    date = models.DateField(blank=True, null=True)  # 달력에서 날짜 부분
    contents = models.CharField(max_length=1000)  # todolist작성내용

    class Meta:
        db_table = "STUDY_PLAN"

    def __str__(self):
        return self.contents