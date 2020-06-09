from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'image', 'author', 'slug',
                    'date_published', 'date_updated')
    search_fields = ('title', 'body',)
    readonly_fields = ('date_published', 'date_updated')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Post, PostAdmin)
