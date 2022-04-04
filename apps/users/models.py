from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser

class Department(models.Model):
    """
    科室分类
    """
    CATEGORY_TYPE = (
        (1, "一级类目"),
        (2, "二级类目"),
    )
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=30, verbose_name='科室分类名')
    category_type = models.IntegerField(choices=CATEGORY_TYPE,verbose_name="类目级别")
    # 设置models有一个指向自己的外键
    parent_type = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, verbose_name="父类目级别",
                                        related_name="sub_cat")
    class Meta:
        ordering = ['id']
        verbose_name = "科室"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class UserInfo(AbstractUser):
    """
    用户信息
    """
    GENDER_CHOICES = (
        ("1", "男"),
        ("2", "女")
    )
    name = models.CharField("姓名",max_length=30)
    birthday = models.DateField("出生年月", null=True)
    gender = models.CharField("性别",max_length=6, choices=GENDER_CHOICES, default='1')
    mobile = models.CharField("电话",max_length=11,help_text='手机号', null=True)
    email = models.EmailField("邮箱",max_length=100, null=True)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class PatientInfo(models.Model):
    """
    患者信息
    """

    GENDER_CHOICES = (
        ("1", "男"),
        ("2", "女")
    )
    desc = models.CharField("病况描述", max_length=500)
    name = models.CharField("患者姓名", max_length=10)
    age = models.IntegerField("年龄", max_length=3)
    height = models.DecimalField("身高", max_digits=5, decimal_places=2)
    weight = models.DecimalField("体重", max_digits=5, decimal_places=2)
    gender = models.CharField("性别",max_length=6, choices=GENDER_CHOICES, default='1')
    supplement = models.CharField("补充细节", max_length=256)
    depart = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True, verbose_name='会诊科室')

    class Meta:
        verbose_name = "患者信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name





# class VerifyCode(models.Model):
#     """
#     验证码
#     """
#     code = models.CharField("验证码",max_length=10)
#     mobile = models.CharField("电话",max_length=11)
#     add_time = models.DateTimeField("添加时间",default=datetime.now)

#     class Meta:
#         verbose_name = "短信验证"
#         verbose_name_plural = verbose_name

#     def __str__(self):
#         return self.code
