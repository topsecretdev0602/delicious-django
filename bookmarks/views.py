from django.shortcuts import render


from bookmarks.models import Bookmark
from taggit.models import Tag


def bookmark_list(request):
    bookmarks = Bookmark.objects.all()
    tags = Tag.objects.all()
    context = {
        'bookmarks': bookmarks,
        'tags': tags
    }
    return render(request, 'bookmarks/bookmark_list.html', context)
