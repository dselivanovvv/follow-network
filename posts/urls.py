from django.urls import path

from posts.views import posts_of_following_profiles, PostDetailView

app_name = 'posts'

urlpatterns = [
    path('', posts_of_following_profiles, name='posts-follow-view'),
    path('<str:post_slug>/', PostDetailView.as_view(), name='post_detail-view'),
]