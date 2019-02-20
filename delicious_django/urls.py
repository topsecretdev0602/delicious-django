from django.contrib import admin
from django.urls import path

from bookmarks.views import BookmarkList, BookmarkListByTag, create_bookmark, edit_bookmark, delete_bookmark

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BookmarkList.as_view(), name='bookmarks'),
    path('tags/', BookmarkListByTag.as_view(), name='bookmarks_by_tag'),
    path('create/', create_bookmark),
    path('edit/<slug:slug>/', edit_bookmark),
    path('delete/<slug:slug>/', delete_bookmark),
]
