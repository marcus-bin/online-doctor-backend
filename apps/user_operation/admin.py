from django.contrib import admin

from apps.user_operation.models import UserFav, UserInfo, UserLeavingMessage

# Register your models here.
admin.site.register(UserFav)
admin.site.register(UserInfo)
admin.site.register(UserLeavingMessage)

