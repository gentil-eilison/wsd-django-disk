from django.db import models


class RecordLabel(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')

    class Meta:
        verbose_name = 'Record Label'
        verbose_name_plural = 'Record Labels'
    
    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=150, verbose_name="Name")
    description = models.TextField(verbose_name='Description')
    record_label = models.ForeignKey(to=RecordLabel, related_name='albums', on_delete=models.CASCADE)
    release_year = models.PositiveIntegerField(verbose_name='Release year')
    country = models.CharField(max_length=150, verbose_name='Country')
    genre = models.CharField(max_length=60, verbose_name='Genre')
    amount_produced = models.PositiveIntegerField(verbose_name='Amount')

    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Albums'

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=150, verbose_name='Name')
    albums = models.ManyToManyField(to=Album, related_name='artists')

    class Meta:
        verbose_name = 'Artist'
        verbose_name_plural = 'Artists'
    
    def __str__(self):
        return self.name