from django.urls import path
from . import views

urlpatterns = [
    path("", views.BlogListView.as_view(), name="blogs"),
    path("blogs/", views.BlogListView.as_view(), name="blogs"),
    path("authors/", views.AuthorListView.as_view(), name="authors"),
    path("blogs/<int:pk>", views.BlogDetailView.as_view(), name="blog-detail"),
    path("author/<int:pk>", views.AuthorDetailView.as_view(), name="author-detail"),
]

urlpatterns += [
    path(
        "blogs/<int:pk>/create/", views.CommentCreate.as_view(), name="comment-create"
    ),
]
