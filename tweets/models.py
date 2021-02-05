from django.db import models

class Tweet(models.Model):
  content = models.CharField(max_length=280)
  created = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['-created']

  def __str__(self):
    return self.content if len(self.content) <= 10 else f'{self.content[0:10]}...'
