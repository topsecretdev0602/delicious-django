from django.contrib import admin

from . import models


@admin.register(models.Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['title', 'url']
