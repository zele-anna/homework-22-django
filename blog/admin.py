from django.contrib import admin
from blog.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'views_counter')
    search_fields = ('title', 'text')
