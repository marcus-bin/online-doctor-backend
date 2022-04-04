from django.contrib import admin
from apps.users.models import Department, PatientInfo, UserInfo

# Register your models here.
admin.site.register(Department)
admin.site.register(UserInfo)
admin.site.register(PatientInfo)