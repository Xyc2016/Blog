from django.db import models


# Create your models here.


class Article(models.Model):
    title = models.TextField()
    content = models.TextField()


class FriendLink(models.Model):
    link = models.TextField()


class Message(models.Model):
    author = models.TextField()
    content = models.TextField()


class ArticleComment(models.Model):
    author = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()

