from rest_framework import serializers

from apps.trade.models import Doctor

class DoctorListSerializer(serializers.ModelSerializer):
    """
    医生列表序列化器
    """
    class Meta:
        model = Doctor
        exclude = ['is_tab', 'introduction']


class DoctorSerializer(serializers.ModelSerializer):
    """
    医生详情序列化器
    """

    class Meta:
        model = Doctor
        exclude = ['is_tab']