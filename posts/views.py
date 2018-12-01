from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Post, Vote, Comment
from posts.forms import CommentForm, PostForm


# Create your views here.
def index(request):
    '''
    render posts on home page
    '''

    posts = Post.objects.all()
    return render(request, 'index.html', {
        'posts': posts,
    })


def post_detail(request, id):
    """
    This shows all the comments
    """
    post = Post.objects.get(id=id)
    return render(request, 'comment/post_detail.html', {'post': post})


def add_comment(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', id=post.id)

    else:
        form = CommentForm()
        template = 'comment/add_comment.html'
        context = {'form': form}
        return render(request, template, context,)


def add_post(request):
    form_class = PostForm
    if request.method == "POST":
        form = form_class(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("home",)
    
    else:
        form = form_class()
        return render(request, 'post/add_post.html', {"form": form, })