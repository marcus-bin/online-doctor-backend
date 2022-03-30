from rest_framework import mixins, viewsets
from utils.paginator import ArticleListPagination
from apps.article.models import KnowledgeCat, Article
from apps.article.serializers import KnowledgeCatSerializer, KnowledgeSerializer, ArticleListSerializer, ArticleDetailSerializer
# from rest_framework.pagination import PageNumberPagination




class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    '''
    list:
        知识区分类列表数据
    '''

    queryset = KnowledgeCat.objects.filter(category_type=1).order_by('id')
    serializer_class = KnowledgeCatSerializer
    # # 自定义分页
    # pagination_class = KnowledgeListPagination


class KnowledgeListViewSet(mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    '''
    retrieve:
        文章详情
    '''
    queryset = KnowledgeCat.objects.all()
    #序列化
    serializer_class = KnowledgeSerializer
 

class ArticleViewSet(viewsets.ModelViewSet):
    """
    专家文章【包含全部请求体】
    """
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    # 自定义分页
    pagination_class = ArticleListPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleListSerializer
        else:
            return ArticleDetailSerializer