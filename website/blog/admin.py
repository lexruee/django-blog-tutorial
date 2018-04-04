from django.contrib import admin

from .models import Post, User, Comment

class PostAdmin(admin.ModelAdmin):
    fields = ('author', 'title', 'content', 'pub_date')
    list_display = ('title', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['title']

class CommentAdmin(admin.ModelAdmin):
    fields = ('author', 'post', 'title', 'content', 'pub_date')
    list_display = ('title', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['title']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
