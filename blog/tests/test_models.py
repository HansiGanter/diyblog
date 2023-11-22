from django.test import TestCase
from django.contrib.auth.models import User  # Blog author or commenter
from blog.models import Author, Blog, Comment
import datetime


class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        test_user1 = User.objects.create_user(username="testuser1", password="12345")
        test_user1.save()
        Author.objects.create(user=test_user1, bio="This is a bio")

    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        self.assertEqual(author.get_absolute_url(), "/blog/author/1")

    def test_user_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field("user").verbose_name
        self.assertEqual(field_label, "user")

    def test_bio_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field("bio").verbose_name
        self.assertEqual(field_label, "bio")

    def test_bio_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field("bio").max_length
        self.assertEqual(max_length, 1000)

    def test_object_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = author.user.username
        self.assertEqual(expected_object_name, str(author))


class BlogModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        test_user1 = User.objects.create_user(username="testuser1", password="12345")
        test_user1.save()
        author = Author.objects.create(user=test_user1, bio="This is a bio")
        blog = Blog.objects.create(
            name="Test Blog 1",
            author=author,
            content="Test Blog 1 Description",
            postdate=datetime.date.today(),
        )

    def test_get_absolute_url(self):
        blog = Blog.objects.get(id=1)
        self.assertEqual(blog.get_absolute_url(), "/blog/blogs/1")

    def test_name_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_name_max_length(self):
        blog = Blog.objects.get(id=1)
        max_length = blog._meta.get_field("name").max_length
        self.assertEqual(max_length, 200)

    def test_content_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field("content").verbose_name
        self.assertEqual(field_label, "content")

    def test_content_max_length(self):
        blog = Blog.objects.get(id=1)
        max_length = blog._meta.get_field("content").max_length
        self.assertEqual(max_length, 1000)

    def test_postdate_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field("postdate").verbose_name
        self.assertEqual(field_label, "postdate")

    def test_postdate(self):
        blog = Blog.objects.get(id=1)
        post_date = blog.postdate
        self.assertEqual(post_date, datetime.date.today())

    def test_object_name(self):
        blog = Blog.objects.get(id=1)
        expected_object_name = "{0} ({1}) - {2}".format(
            blog.name, blog.postdate, blog.author
        )
        self.assertEqual(expected_object_name, str(blog))


class CommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        test_user1 = User.objects.create_user(username="testuser1", password="12345")
        test_user1.save()
        test_user2 = User.objects.create_user(username="testuser2", password="12345")
        test_user2.save()
        blog_author = Author.objects.create(user=test_user1, bio="This is a bio")
        blog_test = Blog.objects.create(
            name="Test Blog 1",
            author=blog_author,
            postdate=datetime.date.today(),
            content="Test Blog 1 Description",
        )
        blog_comment = Comment.objects.create(
            content="Test Blog 1 Comment 1 Description",
            author=test_user2,
            blog=blog_test,
        )

    def test_content_label(self):
        blogcomment = Comment.objects.get(id=1)
        field_label = blogcomment._meta.get_field("content").verbose_name
        self.assertEqual(field_label, "content")

    def test_content_max_length(self):
        blogcomment = Comment.objects.get(id=1)
        max_length = blogcomment._meta.get_field("content").max_length
        self.assertEqual(max_length, 500)

    def test_author_label(self):
        blogcomment = Comment.objects.get(id=1)
        field_label = blogcomment._meta.get_field("author").verbose_name
        self.assertEqual(field_label, "author")

    def test_date_label(self):
        blogcomment = Comment.objects.get(id=1)
        field_label = blogcomment._meta.get_field("postdate").verbose_name
        self.assertEqual(field_label, "postdate")

    def test_blog_label(self):
        blogcomment = Comment.objects.get(id=1)
        field_label = blogcomment._meta.get_field("blog").verbose_name
        self.assertEqual(field_label, "blog")

    def test_object_name(self):
        blogcomment = Comment.objects.get(id=1)
        expected_object_name = ""
        len_title = 75
        if len(blogcomment.content) > len_title:
            expected_object_name = blogcomment.content[:len_title] + "..."
        else:
            expected_object_name = blogcomment.content

        self.assertEqual(expected_object_name, str(blogcomment))
