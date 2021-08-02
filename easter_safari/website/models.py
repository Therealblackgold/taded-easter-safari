from django.db import models
from django.utils.safestring import mark_safe


class Post(models.Model):
    image_link = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(
            self.image_link.url))

    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True

    def __str__(self):
        return self.title