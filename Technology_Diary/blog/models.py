from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # author is the user
    title = models.CharField(max_length=255)
    # sub_headline = models.CharField(max_length=500, null=True, blank=True)
    content = RichTextUploadingField()
    publish_date = models.DateTimeField(default=timezone.now)
    # thumbnail = models.ImageField(null=True, blank=True, upload_to="users/thumbnails", default="default.jpg")
    # active = models.BooleanField(default=False)
    # featured = models.BooleanField(default=False)
    # tags = models.ManyToManyField(Tag, null=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):  # dunder(double under score) str method
        return f"{self.title} by {self.author}"

    def get_absolute_url(self):  # redirects to post details after creating a post successfully
        return reverse('post_detail', kwargs={'slug': self.slug})  # reverse() return the full path as a string

    def save(self, *args, **kwargs):
        if self.slug is None:
            slug = slugify(self.title)

            has_slug = Post.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.title) + '-' + str(count)
                has_slug = Post.objects.filter(slug=slug).exists()

            self.slug = slug
        super().save(*args, **kwargs)


class PostComment(models.Model):
    serial_no = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)  # parent of a comment, if none then self
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.comment[:15]} by {self.user}, serial no: {self.serial_no}"


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=500, default="")
    message = models.TextField(default="")
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f'{self.name}, {self.email} at {self.timestamp}'
