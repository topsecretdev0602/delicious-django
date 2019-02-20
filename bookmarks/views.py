from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.urls import reverse

from bookmarks.forms import BookmarkModelForm
from bookmarks.models import Bookmark


class BookmarkList(generic.ListView):
    template_name = 'bookmarks/bookmark_list.html'
    queryset = Bookmark.objects.all()


class BookmarkListByTag(generic.ListView):
    template_name = 'bookmarks/bookmark_list.html'

    def get_queryset(self):
        tag = self.request.GET.get('tag')
        queryset = Bookmark.objects.filter(tags__name__in=[tag])
        return queryset


def create_bookmark(request):
    form = BookmarkModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(reverse('bookmarks'))
    context = {
        'form': form
    }
    return render(request, 'bookmarks/create_bookmark.html', context)


def edit_bookmark(request, slug):
    bookmark = get_object_or_404(Bookmark, slug=slug)
    form = BookmarkModelForm(request.POST or None, instance=bookmark)
    if form.is_valid():
        form.save()
        return redirect(reverse('bookmarks'))
    context = {
        'form': form
    }
    return render(request, 'bookmarks/create_bookmark.html', context)


def delete_bookmark(request, slug):
    bookmark = get_object_or_404(Bookmark, slug=slug)
    bookmark.delete()
    return redirect(reverse('bookmarks'))
