# Register your models here.
from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # отображение списка статей в панели админа, поиск и фильтр
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('created', 'status', 'publish', 'slug', 'author')
    search_fields = ('title', 'body')
    # автоподбор поля slug по полю title
    prepopulated_fields = {'slug': ('title',)}
    # подбор автора по списку
    raw_id_fields = ('author',)
    # сортировка записей списка статей
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
