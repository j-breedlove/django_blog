from django.urls import path

from blog import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts/", views.posts_page, name="posts-page"),
    path("posts/<slug:post_id>/", views.post_details, name="post-details")

]