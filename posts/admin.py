from django.contrib import admin
from posts.models import Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    '''
    shows post fields in the admin
    '''
    model = Post
    list_display = ('title', 'post_link', 'user', 'score')


admin.site.register(Post)
