from django.urls import path

from posts.views import posts_of_following_profiles, PostDetailView, PostCreate

app_name = 'posts'

urlpatterns = [
    path('', posts_of_following_profiles, name='posts-follow-view'),
    path('create_post/', PostCreate.as_view(), name='post-create-view'),
    path('<str:post_slug>/', PostDetailView.as_view(), name='post-detail-view'),
]