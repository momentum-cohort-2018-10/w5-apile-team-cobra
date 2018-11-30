from django.shortcuts import render
from posts.models import Post, Vote, Comment


# Create your views here.
def index(request):
    '''
    render posts on home page
    '''

    posts = Post.objects.all()
    return render(request, 'index.html', {
        'posts': posts,
    })


def comment_detail(request, id):
    """
    This shows all the comments
    """
    comment = Comment.objects.get(pk=id)
    return render(request, 'comment/comment_detail.html', {'comment': comment})