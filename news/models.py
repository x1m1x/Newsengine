from django.db import models
from django.shortcuts import reverse

from time import time

def gen_slug(s):
    return s.replace(" ", "-") + "-" + str(int(time())) if " " in s else s

def gen_comment_slug(author_name, body):
    return author_name.replace(" ", "-") + "-" + str(int(time())) + "-" + str(body) if " " in author_name else author_name + "-" + str(int(time()))

class Article(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField(blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True)
    image = models.ImageField(upload_to='', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('article_detail_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('article_delete_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('article_update_url', kwargs={'slug': self.slug})

    def get_create_comment_url(self):
        return reverse('article_comment_create_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    author_name = models.CharField(max_length=50)
    body = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.author_name

    def get_delete_url(self):
        return reverse('article_comment_delete_url', kwargs={'slug': self.article.slug, 'comment_slug': self.slug})

    def get_update_url(self):
        return reverse('article_comment_update_url', kwargs={'slug': self.article.slug, 'comment_slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_comment_slug(self.author_name, self.body[:5])
        super().save(*args, **kwargs)
