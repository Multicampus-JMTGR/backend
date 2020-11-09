from rest_framework import serializers
from .models import User, StudyPlan
from certificate.models import Certificate, Category
from certificate.serializers import CertificateSerializer, CategorySerializer, CertScheduleSerializer

# 유저 기본 정보       
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# 유저 정보 + 유저가 좋아요 한 자격증, 카테고리 목록
class UserLikesSerializer(serializers.ModelSerializer):
    cert_likes = CertificateSerializer(many=True, read_only=True)
    cat_likes = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('email', 'interest', 'name', 'phone_number', 'cat_likes', 'cert_likes')

# 스터디 플랜만
class StudyPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyPlan
        fields = ('content', 'email', 'cert', 'date', 'contents')

# 유저 정보 + 좋아요 한 자격증, 카테고리 목록, 스터디 플랜
class UserLikesStudySerializer(serializers.ModelSerializer):
    cert_likes = CertificateSerializer(many=True, read_only=True)
    cat_likes = CategorySerializer(many=True, read_only=True)
    study_plan = StudyPlanSerializer(many=True, read_only = True)

    class Meta:
        model = User
        fields = ('email', 'interest', 'name', 'phone_number', 'cat_likes', 'cert_likes', 'study_plan')


    # def update(self, instance, validated_data, cert_id):
    #     # cert_id가 이미 좋아요 한 게시물중에 있는지 필터 기능을 써서 확인하기
    #     like_exists = validated_data.filter('cert_likes', cert_id)

    #     # 좋아요가 아닌 다른 요청 값들은 validated_data에서 불러오기
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.interest = validated_data.get('interest', instance.interest)
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.phone_number = validated_data.get('phone_number', instance.phone_number)
    #     instance.cat_likes = validated_data.get('cat_likes', instance.cat_likes)
    #     instance.cert_likes = validated_data.get('cert_likes', instance.cert_likes)

    #     #만약 cert_id가 좋아요한 게시물 목록에 없다면 추가, 있다면 삭제
    #     if like_exists == "":
    #         instance.cert_likes.add(cert_id)
    #     else:
    #         instance.cert_likes.remove(cert_id)
        
    #     instance.save() #instance 저장
    #     return instance
