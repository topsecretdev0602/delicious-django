from django import forms

from bookmarks.models import Bookmark


class BookmarkModelForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = ['title', 'url', 'description', 'tags']
