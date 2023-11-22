from django.contrib import admin

# Register your models here.

from .models import Author, Blog, Comment

"""Minimal registration of Models.
admin.site.register(Blog)
admin.site.register(Author)
"""


class BlogsInline(admin.TabularInline):
    """Defines format of inline blog insertion (used in AuthorAdmin)"""

    model = Blog
    extra = 0


class CommentsInline(admin.TabularInline):
    """Defines format of inline blog insertion (used in AuthorAdmin)"""

    model = Comment
    extra = 0


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Administration object for Author models.
    Defines:
     - fields to be displayed in list view (list_display)
     - orders fields in detail view (fields),
       grouping the date fields horizontally
     - adds inline addition of blogs in author view (inlines)
    """

    fields = ["user", "bio"]
    inlines = [BlogsInline]


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """Administration object for Blog models.
    Defines:
     - fields to be displayed in list view (list_display)
     - adds inline addition of blog instances in blog view (inlines)
    """

    list_display = ("name", "author", "postdate")
    inlines = [CommentsInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Administration object for Comment models.
    Defines:
     - fields to be displayed in list view (list_display)
     - adds inline addition of comment instances in comment view (inlines)
    """

    list_display = ("blog", "author", "postdate")
