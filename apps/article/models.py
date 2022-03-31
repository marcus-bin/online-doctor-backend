from datetime import datetime
from django.db import models

from apps.users.models import Department
# 替换系统自带user
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.

class Article(models.Model):
    """专家文章"""
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='articles', verbose_name='作者')
    title = models.CharField(max_length=100)
    body = models.TextField(verbose_name='正文')
    fav_num = models.IntegerField(default=0, verbose_name='收藏数')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    category = models.ForeignKey('KnowledgeCat', on_delete=models.SET_NULL,null=True, blank=True, related_name='cates', verbose_name='文章分类')
    
    class Meta:
        ordering = ['-create_time']
        verbose_name = '专家文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

class KnowledgeCat(models.Model):
    """
    知识科普
    """
    CATEGORY_TYPE = (
        (1, "一级类目"),
        (2, "二级类目")
    )
    # 目录级别
    id = models.AutoField(max_length=10, unique=True, primary_key=True)
    category_type = models.IntegerField(choices=CATEGORY_TYPE,verbose_name="类目级别")
    # 设置models有一个指向自己的外键
    parent_type = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE,  verbose_name="父类目级别", help_text="父目录",
                                        related_name="sub_cat")
    name = models.CharField(max_length=20, verbose_name='分类名', default='疾病')
    body = models.TextField(verbose_name='知识区文章', null=True, blank=True)
    depart = models.ManyToManyField(Department, null=True, blank=True, related_name='departs', verbose_name='相关科室')
    class Meta:
        ordering = ['id']
        verbose_name = "知识科普区"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

