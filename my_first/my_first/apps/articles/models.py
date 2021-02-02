from django.conf import settings
from django.db import models
from django.utils import timezone
import datetime


class Article(models.Model):
    article_title = models.CharField('Название статьи', max_length=200)
    article_text = models.TextField('Текст статьи')
    article_pub_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.article_pub_date >= (timezone.now() - datetime.timedelta(days=7))

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment_author = models.CharField('Автор комментария', max_length=50)
    comment_text = models.CharField('Текст комментария', max_length=200)

    def __str__(self):
        return self.comment_author

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
