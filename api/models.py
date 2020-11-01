from django.conf import settings
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

# 자격증 카테고리 예) 정보통신
class Category(models.Model):
    cat_id = models.IntegerField(primary_key=True, max_length=500) #PK(카테고리PK)
    name = models.CharField(max_length=50) #카테고리 이름

    class Meta:
        db_table = 'CATEGORY'

    def __str__(self):
        return self.name

# 세부 자격증 예) 정보처리기사
class Certificate(models.Model):
    cert_id = models.IntegerField(primary_key=True, max_length=50) #PK(자격증PK)
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE) #FK(카테고리PK)
    name = models.CharField(max_length=100) #자격증 이름
    department = models.CharField(max_length=100) #시행기관
    pass_percent = models.FloatField(max_length=50) #합격률
    cost = models.IntegerField(max_length=100) #응시료

    class Meta:
        db_table = "CERTIFICATE"

    def __str__(self):
        return self.name

# 자격증 접수일정 정보
class Schedule:
    schedule_id = models.IntegerField(primary_key=True, max_length=500) #PK(접수일정PK)
    cert_id = models.ForeignKey(Certificate, on_delete=models.CASCADE) #FK(자격증PK)
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE) #FK(카테고리PK)
    필기접수 = models.DateField #필기접수 날짜
    필기시험 = models.DateField #필기시험 날짜
    필기결과 = models.DateField #필기결과 날짜
    실기접수 = models.DateField #실기접수 날짜
    실기시험 = models.DateField #실기시험 날짜
    실기결과 = models.DateField #실기결과 날짜
    회차 = models.IntegerField(max_length=50) #회차(숫자?)

    class Meta:
        db_table = "SCHEDULE"



# 관심 자격증 표시 여부
# ondelete 설명 : https://lee-seul.github.io/django/backend/2018/01/28/django-model-on-delete.html
class Likes:
    # FK두개 합쳐 하나의 PK를 이룸
    id_token = models.ForeignKey(User, on_delete=models.CASCADE) #FK(사용자PK)
    cert_id = models.ForeignKey(Certificate, on_delete=models.CASCADE) #FK(자격증PK)

    class Meta:
        db_table = "LIKES"




# 스터디 플랜
# ondelete 설명 : https://lee-seul.github.io/django/backend/2018/01/28/django-model-on-delete.html
class StudyPlan(models.Model):
    content_id = models.CharField(max_length=50) #PK(스터디플랜PK)
    id_token = models.ForeignKey(User, on_delete=models.CASCADE) #FK(사용자PK)
    cert_id = models.ForeignKey(Certificate, on_delete=models.CASCADE) #FK(자격증PK)
    date = models.DateField #달력에서 날짜 부분
    contents = models.CharField(max_length=1000) #todolist작성내용

    class Meta:
        db_table = "STUDY_PLAN"

    def __str__(self):
        return self.contents







