from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User  # Blog author or commenter


class Blog(models.Model):
    """Model representing a blog post."""

    name = models.CharField(max_length=200)
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)
    postdate = models.DateField()
    content = models.TextField(max_length=1000, help_text="Enter your blog here...")

    class Meta:
        ordering = ["-postdate"]

    def get_absolute_url(self):
        """Returns the url to access a particular blog instance."""
        return reverse("blog-detail", args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return "{0} ({1}) - {2}".format(self.name, self.postdate, self.author)


class Author(models.Model):
    """Model representing an author."""

    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=1000, help_text="Enter your bio here...")

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse("author-detail", args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.user.username


class Comment(models.Model):
    """Model representing a blog comment"""

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    postdate = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=500, help_text="Add your comment here.")

    class Meta:
        ordering = ["postdate"]

    def get_absolute_url(self):
        """Returns the url to the associated blog instance."""
        return reverse("blog-detail", args=[str(self.blog.id)])

    def __str__(self):
        """String for representing the Model object."""
        len_title = 75
        if len(self.content) > len_title:
            titlestring = self.content[:len_title] + "..."
        else:
            titlestring = self.content
        return titlestring
