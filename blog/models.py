from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Содержимое', null=True, blank=True)
    image = models.ImageField(upload_to='blog/images', verbose_name='Превью', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    is_published = models.BooleanField(verbose_name='Признак публикации', default='True')
    views_counter = models.IntegerField(verbose_name='Количество просмотров', default=0)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['title', 'created_at']

    def __str__(self):
        return self.title
