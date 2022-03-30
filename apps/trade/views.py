from rest_framework import mixins, viewsets
from apps.trade.serializers import DoctorListSerializer, DoctorSerializer

from apps.trade.models import Doctor

# Create your views here.
class DoctorViewSet(viewsets.ModelViewSet):
    """
    医生区块【包含全部请求体】
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorListSerializer
    # 自定义分页
    # pagination_class = ArticleListPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return DoctorListSerializer
        else:
            return DoctorSerializer