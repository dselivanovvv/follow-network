from django.db import models
from django.contrib.auth.models import User

# from posts.models import Post
from django.urls import reverse


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    following = models.ManyToManyField(User, related_name='following', blank=True)
    read = models.ManyToManyField('posts.Post', related_name='read', blank=True)
    bio = models.TextField(default='no bio...')
    created = models.DateTimeField(auto_now_add=True)

    def profiles_posts(self):
        return self.post_set.all()

    def get_absolute_url(self):
        return reverse('profiles:profile-detail-view', kwargs={'username': self.user.username})

    def __str__(self):
        return str(self.user.username)

    class Meta:
        ordering = ('-created',)
