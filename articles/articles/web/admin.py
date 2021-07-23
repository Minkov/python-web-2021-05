from django.contrib import admin

from articles.web.models import Article, Source


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    pass
