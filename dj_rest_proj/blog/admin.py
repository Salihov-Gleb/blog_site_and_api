from django.contrib import admin

from .models import BlogNote, Category


class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'update_date', 'img']
    list_display_links = ['id', 'title']
    # prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']


admin.site.register(BlogNote, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
