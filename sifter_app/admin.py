from django.contrib import admin
from .models import User, Source, Category
from  django.contrib.auth.admin import UserAdmin


admin.site.register(User, UserAdmin)


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'language', 'url')
    list_editable = ('country', 'language', 'url')
    list_filter = ('country', 'language')
    list_display_links = ['name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)