from django.db import models


class Word(models.Model):

    class Meta:
        verbose_name = 'Слово'
        verbose_name_plural = 'Слова'
        ordering = ['russian', 'english']

    russian = models.CharField(max_length=255, verbose_name='word1')
    english = models.CharField(max_length=255, verbose_name='word2')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')
    time_update = models.DateTimeField(auto_now_add=True, verbose_name='Время изменения')