from django.db import models
from users.models import User


class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=280)
    likes = models.ManyToManyField(
        User, blank=True, related_name='tweet_likes')
    likes_total = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content if len(self.content) <= 10 else f'{self.content[0:10]}...'
