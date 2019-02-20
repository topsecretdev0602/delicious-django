from django.db import models
from django.template.defaultfilters import slugify

from taggit.managers import TaggableManager


class Bookmark(models.Model):
    title = models.CharField(default='', blank=True, max_length=255)
    url = models.URLField('URL')
    description = models.TextField(default='', blank=True)
    slug = models.SlugField(unique=True)

    tags = TaggableManager()

    def __str__(self):
        return self.title if self.title else self.url

    # overriding save to auto fill in the slug for each bookmark
    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.title)

        super(Bookmark, self).save(*args, **kwargs)

    # helper function to get edit URL
    def get_edit_url(self):
        return "/edit/{}/".format(self.slug)

    # helper function to get delete URL
    def get_delete_url(self):
        return "/delete/{}/".format(self.slug)
