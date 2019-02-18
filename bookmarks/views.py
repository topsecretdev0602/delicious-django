from django.shortcuts import render
from django.views import generic

from bookmarks.models import Bookmark


class BookmarkList(generic.ListView):
    template_name = 'bookmarks/bookmark_list.html'
    queryset = Bookmark.objects.all()