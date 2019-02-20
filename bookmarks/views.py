from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic

from bookmarks.forms import BookmarkModelForm
from bookmarks.models import Bookmark


class BookmarkList(generic.ListView):
    template_name = 'bookmarks/bookmark_list.html'
    queryset = Bookmark.objects.all()


def create_bookmark(request):
    form = BookmarkModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'bookmarks/create_bookmark.html', context)


def edit_bookmark(request, slug):
    bookmark = get_object_or_404(Bookmark, slug=slug)
    form = BookmarkModelForm(request.POST or None, instance=bookmark)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'bookmarks/create_bookmark.html', context)


def delete_bookmark(request, slug):
    bookmark = get_object_or_404(Bookmark, slug=slug)
    bookmark.delete()
    return redirect('/')
