from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class BookList(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publication = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ['name']
