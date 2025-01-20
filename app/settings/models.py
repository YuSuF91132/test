from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    tema = models.CharField(max_length=50, verbose_name='Тема')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'

class Newave(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image1 = models.ImageField(
        upload_to="newave/",
        verbose_name='Фото 1'
    )
    image2 = models.ImageField(
        upload_to="newave/",
        verbose_name='Фото 2'
    )
    image3 = models.ImageField(
        upload_to="newave/",
        verbose_name='Фото 3'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Описание"