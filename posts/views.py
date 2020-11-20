from itertools import chain

from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from posts.models import Post
from profiles.models import Profile


def posts_of_following_profiles(request):
    # get logged in user profile
    profile = Profile.objects.get(user=request.user)
    # check who we are following
    users = [user for user in profile.following.all()]
    # initial values for variables
    posts = []
    qs = None
    # get the posts of people who we are following
    for u in users:
        p = Profile.objects.get(user=u)
        p_posts = p.post_set.all()
        posts.append(p_posts)
    # our posts
    my_posts = profile.post_set.all()
    posts.append(my_posts)

    # sort and chain querysets and unpack the posts list
    if len(posts) > 0:
        qs = sorted(chain(*posts), reverse=True, key=lambda obj: obj.created)

    return render(request, 'posts/main.html', {'profile': profile, 'posts': qs, 'read': profile.read.all()})


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'


    def get_object(self, queryset=None):
        return get_object_or_404(Post, slug=self.kwargs.get('post_slug'))