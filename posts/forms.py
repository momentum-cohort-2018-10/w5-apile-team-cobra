from django.forms import ModelForm
from posts.models import Comment, Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'post_link','user', 'score')


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
