from django.shortcuts import render, redirect
from posts.models import Post, Vote
from django.views.decorators.http import require_POST
from django.db.models import F


# Create your views here.
def index(request):
    '''
    render posts on home page
    '''
    posts = Post.objects.all().order_by('-score')
    return render(request, 'index.html', {
        'posts': posts,
    })

@require_POST
def user_vote(request, id):
    '''
    register a users vote in the post's score
    '''
    # make an instance of the vote based on the post id
    post = Post.objects.get(pk=id)
    # add one to score using query expression
    post.score = F('score') + 1 
    post.save()
    return redirect('home')
