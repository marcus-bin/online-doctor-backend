from unicodedata import category
from django.forms import Field
from rest_framework import serializers
from apps.users.serializers import DepartmentSerializer2
# from apps.article.filters import KnowledgeCatFilter
from apps.article.models import KnowledgeCat, Article

class KnowledgeCatSerializer2(serializers.ModelSerializer):
    '''
    知识区详情二级分类序列化
    '''

    class Meta:
        model = KnowledgeCat
        fields = ['id', 'name']


class KnowledgeCatSerializer(serializers.ModelSerializer):
    """
    知识区一级类别序列化
    """
    
    # 在parent_category字段中定义的related_name="sub_cat"
    sub_cat = KnowledgeCatSerializer2(many=True)

    class Meta:
        model = KnowledgeCat
        fields = ['name', 'sub_cat']
        


class KnowledgeSerializer(serializers.ModelSerializer):
    """
    知识区文章序列化器
    """
    # 与model字段中定义保持一致，不需要使用related_name
    depart = DepartmentSerializer2(many=True, read_only=True)
    
    class Meta:
        model = KnowledgeCat
        fields = ['id', 'body', 'depart', 'name']
        read_only_fields = ['depart']


class ArticleListSerializer(serializers.ModelSerializer):
    """
    专家文章列表序列化器
    """
    cate = serializers.ReadOnlyField(source="category.name")
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Article
        fields = ['id', 'cate', 'title', 'author', 'create_time']
        read_only_fields = ['create_time']
        

class ArticleDetailSerializer(serializers.ModelSerializer):
    """
    专家文章详情序列化器
    """
    cate = serializers.ReadOnlyField(source="category.name")
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Article
        exclude = ['category', 'update_time']
        read_only_fields = ['create_time']
