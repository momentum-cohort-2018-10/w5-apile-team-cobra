from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    '''
    post model
    '''
    title = models.CharField(max_length=255)
    post_link = models.URLField(max_length=255)
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=True)
    user_has_voted = models.ManyToManyField(to=User, through='Vote', related_name='user_vote')
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Vote(models.Model):
    '''
    vote on post
    '''
    voter = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="vote")
    post = models.ForeignKey(to=Post, on_delete=models.SET_NULL, null=True)


class Comment(models.Model):
    '''
    adds coments to post
    '''
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body
