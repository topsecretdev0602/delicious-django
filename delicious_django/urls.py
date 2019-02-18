from django.contrib import admin
from django.urls import path

from bookmarks.views import BookmarkList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BookmarkList.as_view(), name='bookmarks'),
]
