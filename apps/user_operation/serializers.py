from rest_framework import serializers
from apps.article.serializers import ArticleListSerializer
from rest_framework.validators import UniqueTogetherValidator
from apps.user_operation.models import UserFav, UserInfo, UserLeavingMessage

class UserFavDetailSerializer(serializers.ModelSerializer):
    '''
    用户收藏详情
    '''

    #通过文章id获取收藏的文章，需要嵌套文章的序列化
    class Meta:
        model = UserFav
        fields = ("article", "id")


class UserFavSerializer(serializers.ModelSerializer):
    #获取当前登录的用户
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        #validate实现唯一联合，一个商品只能收藏一次
        validators = [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=('user', 'article'),
                message="您已收藏该文章啦"
            )
        ]
        model = UserFav
        #收藏的时候需要返回文章的id，因为取消收藏的时候必须知道文章的id是多少
        fields = ("user", "article",'id')


class LeavingMessageSerializer(serializers.ModelSerializer):
    '''
    用户留言
    '''
    # 获取当前登录的用户
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    # post时候可以不用提交，format：格式化输出
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = UserLeavingMessage
        fields = ("user", "message", "id", "add_time")


class AddressSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = UserInfo
        fields = ("id", "user")

