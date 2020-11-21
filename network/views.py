from django.shortcuts import redirect


def redirect_to_main_page(request):
    return redirect('posts:posts-follow-view')