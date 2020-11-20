from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

from .models import Post
from profiles.models import Profile

