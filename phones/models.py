from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Название')
    price = models.FloatField(verbose_name='Цена')
    image = models.CharField(max_length=100, verbose_name='Изображение')
    release_date = models.DateField(max_length=30, verbose_name='Дата выхода')
    lte_exists = models.BooleanField(verbose_name='Поддержка Lte')
    slug = models.SlugField(verbose_name='URL')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)
