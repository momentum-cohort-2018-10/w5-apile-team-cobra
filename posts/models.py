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


# to = User, through = Vote, related_name = 'user_voted'
class Vote(models.Model):
    '''
    vote on posts
    '''
    voter = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="vote")
    post = models.ForeignKey(to=Post, on_delete=models.SET_NULL, null=True)
    

class Comment(models.Model):
    '''
    adds coments to post
    '''
    pass
