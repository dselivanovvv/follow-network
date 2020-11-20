from time import time

from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from profiles.models import Profile


def generate_slug(title):
    return slugify(title[:20]) + '-' + str(int(time()))


class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, max_length=100)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = generate_slug(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('posts:post-detail-view', kwargs={'post_slug': self.slug})

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ('-created', )
