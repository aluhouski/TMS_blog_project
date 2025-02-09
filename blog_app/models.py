from django.db import models
from django.contrib.auth.models import User



class BaseModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Post(BaseModel):
    title = models.CharField(max_length=200)


class Comment(BaseModel):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)