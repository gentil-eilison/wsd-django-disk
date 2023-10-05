from django.db import models

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=150, verbose_name="Name")
    description = models.TextField(verbose_name='Description')
    record_label = models.CharField(max_length=100, verbose_name='Record label')
    release_year = models.PositiveIntegerField(verbose_name='Release year')
    country = models.CharField(max_length=150, verbose_name='Country')
    genre = models.CharField(max_length=60, verbose_name='Genre')
    amount_produced = models.PositiveIntegerField(verbose_name='Amount')

    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Albums'

    def __str__(self):
        return self.name
