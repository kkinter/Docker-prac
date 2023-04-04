from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# 60
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blogs_posts')

    title = models.CharField(max_length=52)
    slug = models.SlugField(max_length=100)
    body = models.TextField(blank=True, null=True)

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)
    
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['publish']
        # /ref/models/indexes/
        indexes = [
            models.Index(fields=['-publish'])
        ]

    def __str__(self):
        return self.title
