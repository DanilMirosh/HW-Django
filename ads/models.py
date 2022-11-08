from django.db import models


class Ad(models.Model):

    name = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=1000)
    address = models.CharField(max_length=500)
    is_published = models.BooleanField(default=None)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
