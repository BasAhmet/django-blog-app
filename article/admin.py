from encodings import search_function
from re import search
from unittest.util import _MAX_LENGTH
from xml.etree.ElementTree import Comment
from django.contrib import admin
from .models import Article, Comment

# Register your models here.

admin.site.register(Comment)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","author","createDate"]
    list_display_links = ["title","createDate"]
    search_fields = ["title"]
    list_filter = ["createDate"]
    class Meta:
        model = Article

