from django.shortcuts import render
from posts.models import Post, Vote

# Create your views here.
def index(request):
    '''
    render posts on home page
    '''
    posts = Post.objects.all()
    return render(request, 'index.html', {
        'posts': posts,
    })