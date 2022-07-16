from django.db import models


# Create your models here.
class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    title_desc = models.CharField(max_length=5000)
    heading = models.CharField(max_length=200, default="")
    heading_desc = models.CharField(max_length=5000, default="")
    sub_heading = models.CharField(max_length=200, default="")
    sub_heading_desc = models.CharField(max_length=5000, default="")
    publish_date = models.DateField()
    thumbnail = models.ImageField(upload_to="blog/thumbnails", default="")

    def __str__(self):
        return self.title
