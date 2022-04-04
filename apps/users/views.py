from rest_framework import mixins, viewsets
from apps.users.serializers import DepartmentSerializer, PatientInfoDetailSerializer, PatientInfoListSerializer, UserRegSerializer, UserDetailSerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from apps.users.models import Department, PatientInfo
from rest_framework import status, permissions, authentication
from rest_framework.response import Response
from rest_framework_jwt.serializers import jwt_encode_handler,jwt_payload_handler

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()

class DepartmentViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
    list:
        科室分类列表数据
    '''

    queryset = Department.objects.filter(category_type=1)
    serializer_class = DepartmentSerializer


class PationtInfoViewSet(viewsets.ModelViewSet):
    """
    病例列表及详情
    """
    queryset = PatientInfo.objects.all()
    serializer_class = PatientInfoListSerializer

    # 动态选择序列化器
    def get_serializer_class(self):
        if self.action == 'list':
            return PatientInfoListSerializer
        else:
            return PatientInfoDetailSerializer


class UserViewset(mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):
    '''
    用户
    '''
    serializer_class = UserRegSerializer
    queryset = User.objects.all()
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        re_dict["name"] = user.name if user.name else user.username

        headers = self.get_success_headers(serializer.data)

        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    #这里需要动态权限配置
    #1.用户注册的时候不应该有权限限制
    #2.当想获取用户详情信息的时候，必须登录才行
    def get_permissions(self):
        if self.action == "retrieve":
            return [permissions.IsAuthenticated()]
        elif self.action == "create":
            return []

        return []

    #这里需要动态选择用哪个序列化方式
    #1.UserRegSerializer（用户注册），只返回username，会员中心页面需要显示更多字段，所以要创建一个UserDetailSerializer
    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserDetailSerializer
        elif self.action == "create":
            return UserRegSerializer

        return UserDetailSerializer

    #虽然继承了Retrieve可以获取用户详情，但是并不知道用户的id，所有要重写get_object方法
    #重写get_object方法，就知道是哪个用户了
    def get_object(self):
        return self.request.user

    def perform_create(self, serializer):
        return serializer.save()



