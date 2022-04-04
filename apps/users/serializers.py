from rest_framework import serializers
from apps.users.models import Department, PatientInfo, UserInfo
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model

User = get_user_model()

class DepartmentSerializer2(serializers.ModelSerializer):
    """
    二级科室序列化器【只返回科室名】
    """
    class Meta:
        model = Department
        fields = ['id','name']


class DepartmentSerializer(serializers.ModelSerializer):
    """
    科室序列化器【只返回科室名】
    """
    sub_cat = DepartmentSerializer2(many=True)
    
    class Meta:
        model = Department
        fields = ['id', 'name', 'sub_cat']


class UserDetailSerializer(serializers.ModelSerializer):
    """
    用户详情
    """
    class Meta:
        model = UserInfo
        fields = ["name", "gender", "birthday"]


class UserRegSerializer(serializers.ModelSerializer):
    '''
    用户注册
    '''
    #验证用户名是否存在
    username = serializers.CharField(label="用户名", help_text="用户名", required=True, allow_blank=False,
                                    validators=[UniqueValidator(queryset=User.objects.all(), message="用户已经存在")])
    #输入密码的时候不显示明文
    password = serializers.CharField(
        help_text="密码",
        style={'input_type': 'password'},label=True,write_only=True
    )

    class Meta:
        model = UserInfo
        fields = ('username','password')        


class PatientInfoListSerializer(serializers.ModelSerializer):
    """
    病例列表
    """
    class Meta:
        model = PatientInfo
        fields = ['desc']


class PatientInfoDetailSerializer(serializers.ModelSerializer):
    """
    病例详情
    """

    class Meta:
        model = PatientInfo
        fields = "__all__"