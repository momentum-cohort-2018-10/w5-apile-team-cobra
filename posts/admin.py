from django.contrib import admin
from posts.models import Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display =('title', 'post_link')


admin.site.register(Post)
