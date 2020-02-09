from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):

    def __str__(self):
        return self.post_title

    post_title = models.CharField(max_length=200)
    post_content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post', null=True)

class Comment(models.Model):
    post_comment = models.TextField()
    commented_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment', null=True)
    