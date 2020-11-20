from django.urls import path
from .views import ProfileListView, ProfileDetailView, follow_unfollow_profile, read_unread_post

app_name = 'profiles'

urlpatterns = [
    path('', ProfileListView.as_view(), name='profile-list-view'),
    path('switch_follow/', follow_unfollow_profile, name='follow-unfollow-view'),
    path('switch_read/', read_unread_post, name='read-unread-view'),
    path('<str:username>/', ProfileDetailView.as_view(), name='profile-detail-view'),
]