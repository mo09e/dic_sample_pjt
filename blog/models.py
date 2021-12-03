from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField('Title', max_length=150)
    content = models.TextField('Content', max_length=300)
    date = models.DateTimeField('Date', default=timezone.now)

    def __str__(self):
        return self.title
