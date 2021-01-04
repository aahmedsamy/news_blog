from django.contrib import admin

from .models import Author, Category, Blog


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_filter = ['category__name']


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
