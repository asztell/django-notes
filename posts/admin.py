from django.contrib import admin

# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'timestamp', 'updated', 'draft', 'publish', 'image', 'slug']
    list_display_links = ['timestamp', 'updated']
    list_editable = ['title', 'draft', 'publish', 'image']
    list_filter = ['user', 'title', 'publish', 'updated', 'timestamp', 'image']
    search_fields = ['title', 'content']

    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)
