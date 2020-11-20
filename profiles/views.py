from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

from posts.models import Post
from .models import Profile


def follow_unfollow_profile(request):
    if request.method == 'POST':
        my_profile = Profile.objects.get(user=request.user)
        pk = request.POST.get('profile_pk')
        obj = Profile.objects.get(pk=pk)

        if obj.user in my_profile.following.all():
            my_profile.following.remove(obj.user)

            for p in my_profile.read.filter(author=obj):
                my_profile.read.remove(p)

        else:
            my_profile.following.add(obj.user)
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('profiles:profile-list-view')


def read_unread_post(request):
    if request.method == 'POST':
        my_profile = Profile.objects.get(user=request.user)
        pk = request.POST.get('post_pk')
        obj = Post.objects.get(pk=pk)

        if obj in my_profile.read.all():
            my_profile.read.remove(obj)
        else:
            my_profile.read.add(obj)
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('posts:posts-follow-view')


class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles/main.html'
    context_object_name = 'profiles'

    def get_queryset(self):
        return Profile.objects.all().exclude(user=self.request.user)


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/detail.html'

    def get_object(self, **kwargs):
        username = self.kwargs.get('username')
        user = get_object_or_404(User, username=username)
        view_profile = Profile.objects.get(user=user)
        return view_profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        view_profile = self.get_object()
        my_profile = Profile.objects.get(user=self.request.user)
        if view_profile.user in my_profile.following.all():
            follow = True
        else:
            follow = False

        context['follow'] = follow
        context['read'] = my_profile.read.all()

        return context
