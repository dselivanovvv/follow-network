from itertools import chain

from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import DetailView

from posts.forms import PostForm
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


class PostCreate(View):

    form_model = PostForm
    template = 'posts/post_create.html'
    raise_exception = True

    def get(self, request):
        form = self.form_model()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.form_model(request.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save(commit=False)
            new_obj.author = request.user.profile
            new_obj.save()
            return redirect('posts:post-detail-view',
                            post_slug=new_obj.slug)

        return render(request, self.template, context={'form': bound_form})