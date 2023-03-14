from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django_quill.fields import QuillField
import readtime
import uuid


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to='avatars/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True,
                            null=True, auto_created=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Author, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True,
                            null=True, auto_created=True)

    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        if Category.objects.filter(slug=slug).exists():
            self.slug = slug + '-' + slugify(uuid.uuid1())
        else:
            self.slug = slug
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True,
                            null=True, auto_created=True)

    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        if Tag.objects.filter(slug=slug).exists():
            self.slug = slug + '-' + slugify(uuid.uuid1())
        else:
            self.slug = slug
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True,
                            null=True, auto_created=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = QuillField()
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(
        upload_to='images/', blank=True, null=True)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)
    featured = models.BooleanField()
    is_published = models.BooleanField()

    def save(self, *args, **kwargs):
        slug = slugify(self.title)
        if Post.objects.filter(slug=slug).exists():
            self.slug = slug + '-' + slugify(uuid.uuid1())
        else:
            self.slug = slug
        super(Post, self).save(*args, **kwargs)

    def get_read_time(self):
        result = readtime.of_html(self.content.html)
        return result.text

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']


class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
