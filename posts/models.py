from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    '''
    post model
    '''
    title = models.CharField(max_length=255)
    post_link = models.URLField(max_length=255)

    # # dave: i understand what this does but not how to implement it yet
    # def has_voted(self, user):
    #     '''
    #     checks to see if user has voted, on a given post
    #     '''
    #     return self.vote.filter(user=user).count() > 0


class Vote(models.Model):
    '''
    voting model
    '''
    voter = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="vote")
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
