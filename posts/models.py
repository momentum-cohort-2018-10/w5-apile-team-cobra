from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    '''
    post model
    '''
    title = models.CharField(max_length=255)
    post_link = models.URLField(max_length=255)
    user_has_voted = models.ManyToManyField(to=User, through='Vote', related_name='user_voted')


# to = User, through = Vote, related_name = 'user_voted'
class Vote(models.Model):
    '''
    vote on posts
    '''
    voter = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="vote")
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)


# class Comment(models.Model):
#     '''
#     adds coments to posts
#     '''
#     post = models.ForeignKey(Post, related_name='comments')
# 	user = models.CharField(max_length=255)
# 	email = models.EmailField()
# 	body = models.TextField()
# 	created = models.DateTimeField(auto_now_add=True)
	
# 	def __str__(self):
# 		return self.user