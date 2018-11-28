from django.contrib import admin
from posts.models import Post,Comment


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display =('title', 'post_link')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'body', 'created')

admin.site.register(Post)
admin.site.register(Comment)