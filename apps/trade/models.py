from datetime import datetime
from django.db import models
from apps.users.models import Department
from django.db.models.deletion import SET_NULL

# get_user_model方法会去setting中找AUTH_USER_MODEL
from django.contrib.auth import get_user_model

User = get_user_model()


class Doctor(models.Model):
    """
    医生主页
    """
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='关联用户id')
    department = models.ForeignKey(Department,on_delete=SET_NULL, null=True, verbose_name='所属科室')
    head = models.ImageField(upload_to='doctor/')
    name = models.CharField(max_length=45, verbose_name='姓名') 
    is_tab = models.BooleanField(default=False, verbose_name="是否为推荐医生")
    registration_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='预约费用')
    introduction = models.CharField(max_length=500,verbose_name='个人简介')
    good_at = models.CharField(max_length=500, verbose_name='擅长')
    fav_num = models.IntegerField(default=0, verbose_name='关注数')

    class Meta:
        verbose_name = "医生主页"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



class OrderInfo(models.Model):
    """
    订单信息
    """
    ORDER_STATUS = (
        ("TRADE_SUCCESS", "成功"),
        ("TRADE_CLOSED", "超时关闭"),
        ("WAIT_BUYER_PAY", "交易创建"),
        ("TRADE_FINISHED", "交易结束"),
        ("paying", "待支付"),
    )
    PAY_TYPE = (
        ("alipay", "支付宝"),
        ("wechat", "微信"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    #订单号唯一
    order_sn = models.CharField("订单编号",max_length=30, null=True, blank=True, unique=True)
    # 微信支付会用到
    nonce_str = models.CharField("随机加密串",max_length=50, null=True, blank=True, unique=True)
    # 支付宝交易号
    trade_no = models.CharField("交易号",max_length=100, unique=True, null=True, blank=True)
    #支付状态
    pay_status = models.CharField("订单状态",choices=ORDER_STATUS, default="paying", max_length=30)
    # 订单的支付类型
    pay_type = models.CharField("支付类型",choices=PAY_TYPE, default="alipay", max_length=10)
    post_script = models.CharField("订单留言",max_length=200)
    order_mount = models.FloatField("订单金额",default=0.0)
    pay_time = models.DateTimeField("支付时间",null=True, blank=True)

    # 用户信息
    address = models.CharField("收货地址",max_length=100, default="")
    signer_name = models.CharField("签收人",max_length=20, default="")
    singer_mobile = models.CharField("联系电话",max_length=11)

    add_time = models.DateTimeField("添加时间",default=datetime.now)

    class Meta:
        verbose_name = "订单信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order_sn)


class OrderGoods(models.Model):
    """
    订单内的医生详情
    """
    # 一个订单对应多个商品
    order = models.ForeignKey(OrderInfo, on_delete=models.CASCADE, verbose_name="订单信息", related_name="goods")
    # 两个外键形成一张关联表
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="预约医生")
    add_time = models.DateTimeField("添加时间",default=datetime.now)

    class Meta:
        verbose_name = "预约医生"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order.order_sn)