from django.shortcuts import render
from django.views import generic
from .models import Blog, Author, Comment
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404


# Create your views here.


class BlogListView(generic.ListView):
    """View function for home page of site."""

    model = Blog
    paginate_by = 5


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 5


class BlogDetailView(generic.DetailView):
    model = Blog


class AuthorDetailView(generic.DetailView):
    model = Author


class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ["content"]

    def get_context_data(self, **kwargs):
        """
        Add associated blog to form template so can display its title in HTML.
        """
        # Call the base implementation first to get a context
        context = super(CommentCreate, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context["blog"] = get_object_or_404(Blog, pk=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        """
        Add author and associated blog to form data before setting it as valid (so it is saved to model)
        """
        # Add logged-in user as author of comment
        form.instance.author = self.request.user
        # Associate comment with blog based on passed id
        form.instance.blog = get_object_or_404(Blog, pk=self.kwargs["pk"])
        # Call super-class form validation behavior
        return super(CommentCreate, self).form_valid(form)
