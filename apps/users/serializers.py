from rest_framework import serializers
from apps.users.models import Department


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
        fields = ['name', 'sub_cat']
