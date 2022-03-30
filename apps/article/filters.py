# import django_filters
# from apps.article.models import Knowledge
# from django.db.models import Q

# class KnowledgeCatFilter(django_filters.rest_framework.FilterSet):
#     '''
#     知识区过滤的类
#     '''
#     top_category = django_filters.NumberFilter(field_name='category', method='top_category_filter')

#     def top_category_filter(self, queryset, name, value):
#         # 不管当前点击的是一级分类二级分类还是三级分类，都能找到。
#         return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(
#             category__parent_category__parent_category_id=value))

#     class Meta:
#         model = Knowledge
#         fields = "__all__"