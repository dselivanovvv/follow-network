from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from network.settings import EMAIL_HOST_USER
from .models import Post


@receiver(post_save, sender=Post)
def send_email(sender, instance, created, **kwargs):
    if created:
        # TODO in production uncomment next line
        # recipients = list(email['email'] for email in User.objects.values('email') if email['email'])

        subject = 'New post on network by {}! See it!'.format(instance.author.user.username)
        html_message = render_to_string('posts/mail.html', {'post': instance})
        plain_message = strip_tags(html_message)
        from_email = EMAIL_HOST_USER

        # TODO in production comment next line
        recipients = ['dselivanov2000@gmail.com',]

        send_mail(subject, plain_message, from_email, recipients, html_message=html_message, fail_silently=False)
