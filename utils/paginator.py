from rest_framework.pagination import PageNumberPagination

class ArticleListPagination(PageNumberPagination):
    '''
    知识分类列表自定义分页
    '''
    #默认每页显示的个数
    page_size = 2
    #可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    #页码参数
    page_query_param = 'page'
    #最多能显示多少页
    max_page_size = 100