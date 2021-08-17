from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class BaseModel(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    video = models.FileField(upload_to="videos/", null=True, blank=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True)

    class Meta:
        abstract = True


class Post(BaseModel):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True,)

    def number_of_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return f"{self.title} by {self.author}"

    def get_absolute_url(self):
        return reverse('blogapp-home')


class Comment(BaseModel):
    onPost = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='post_comments', null=True, blank=True, default=None)
    onComment = models.ForeignKey(
        "self", on_delete=models.CASCADE, related_name='comment_comments', null=True, blank=True, default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='comment_like')

    def number_of_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return f"Comment by {self.author.username}"
