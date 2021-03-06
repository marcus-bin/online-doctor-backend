from datetime import datetime
from django.db import models
from apps.article.models import Article

from django.contrib.auth import get_user_model

from apps.trade.models import Doctor
User = get_user_model()


class UserFav(models.Model):
    """
    用户收藏操作
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    goods = models.ForeignKey(Doctor, on_delete=models.CASCADE, null = True, blank = True,verbose_name="关注医生id", help_text="医生id")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null = True, blank = True, verbose_name='收藏文章id')
    add_time = models.DateTimeField("添加时间",default=datetime.now)


    class Meta:
        ordering = ['-add_time']
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name
        unique_together = ("user", "goods")

    def __str__(self):
        return self.user.username


class UserInfo(models.Model):
    """
    用户个人中心资料
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='关联用户')
    real_name = models.CharField("真实姓名", max_length=10, default='')
    mobile = models.IntegerField('手机号', max_length=11, default='')
    
    class Meta:
        ordering = ['id']
        verbose_name='个人中心'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.real_name


class UserLeavingMessage(models.Model):
    """
    用户留言
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="关联医生")
    message = models.TextField("留言内容",default="",help_text="留言内容")
    add_time = models.DateTimeField("添加时间",default=datetime.now)

    class Meta:
        ordering = ['-add_time']
        verbose_name = "用户留言"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.doctor.name