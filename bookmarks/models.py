from django.db import models

from taggit.managers import TaggableManager


class Bookmark(models.Model):
    title = models.CharField(default='', blank=True, max_length=255)
    url = models.URLField('URL')
    description = models.TextField(default='', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    tags = TaggableManager()

    def __str__(self):
        return self.title if self.title else self.url
