# Project: MySuperDjangoProject
# Site: OlegSite
# Author: Oleg Sakharov
# Date: 20/10/2019


from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class Post(models.Model):
    # варианты ответов для поля status
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    # при удалении связанного пользователя база данных также удаляет написанные им статьи
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager()  # менеджер по умолчанию
    published = PublishedManager()  # наш новый менеджер

    # построение канонического URL'а для статей post_detail
    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month, self.publish.day,
                             self.slug])


class Meta:
    ordering = ('-publish',)


def __str__(self):
    return self.title
