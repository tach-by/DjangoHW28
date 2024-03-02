from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()


class Category(models.Model):
    name = models.CharField(max_length=200)


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
