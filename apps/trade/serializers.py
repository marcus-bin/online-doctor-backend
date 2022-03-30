from rest_framework import serializers

from apps.trade.models import Doctor

class DoctorListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Doctor
        exclude = ['is_tab', 'introduction']


class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        exclude = ['is_tab']