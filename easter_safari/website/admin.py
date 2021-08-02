from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    # fields = ('admin_photo', 'title', 'image')
    list_display = ['admin_photo', 'title', 'image_link']
    list_display_links = ['admin_photo', 'title']
    readonly_fields = ['admin_photo']


admin.site.register(Post, PostAdmin)
