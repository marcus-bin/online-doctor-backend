"""Onlinedoctor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.user_operation.views import LeavingMessageViewset, UserFavViewset
from apps.users.views import DepartmentViewSet, UserViewset
from apps.article.views import  CategoryViewSet, KnowledgeListViewSet, ArticleViewSet
from apps.trade.views import DoctorViewSet

router = DefaultRouter()
# 配置知识区分类的url
router.register(r'knowledgecat', CategoryViewSet, basename="knowledgecat")
# 配置知识区详情的url
router.register(r'knowledge', KnowledgeListViewSet,basename="knowledge")
# 配置科室分类的url
router.register(r'department', DepartmentViewSet, basename='department')
# 配置文章列表及详情的url
router.register(r'article', ArticleViewSet, basename="article")
# 配置医生列表及详情的url
router.register(r'doctor', DoctorViewSet, basename="doctor")
#配置用户的url
router.register(r'users', UserViewset, basename="users")
# 配置用户收藏的url
router.register(r'userfavs', UserFavViewset, basename="userfavs")
# 配置用户留言的url
router.register(r'messages', LeavingMessageViewset, basename="messages")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    # token
    path('api-token-auth/', views.obtain_auth_token),
    #drf文档，title自定义
    path('docs',include_docs_urls(title='康乐api接口文档')),
    # jwt的token认证接口
    path('login/', obtain_jwt_token)
]

# 文件路由
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)