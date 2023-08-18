from django.shortcuts import render


# Create your views here.
def starting_page(request):
    return render(request, 'blog/index.html')


def posts_page(request):
    return render(request, 'blog/posts-page.html')


def post_details(request, post_id):
    return render(request, 'blog/post-details.html')
