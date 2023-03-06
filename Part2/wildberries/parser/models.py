from django.db import models


class Products(models.Model):
    article = models.IntegerField(verbose_name='Артикул')
    brand = models.CharField(max_length=255, verbose_name='Бренд')
    title = models.CharField(max_length=255, verbose_name='Название артикула')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
