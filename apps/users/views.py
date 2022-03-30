from rest_framework import mixins, viewsets
from apps.users.serializers import DepartmentSerializer

from apps.users.models import Department

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q


class DepartmentViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
    list:
        知识区分类列表数据
    '''

    queryset = Department.objects.filter(category_type=1)
    serializer_class = DepartmentSerializer
