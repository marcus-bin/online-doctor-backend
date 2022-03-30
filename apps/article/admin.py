from django.contrib import admin
from apps.article.models import KnowledgeCat,Article
# Register your models here.

admin.site.register(KnowledgeCat)
admin.site.register(Article)