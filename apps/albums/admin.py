from django.contrib import admin
from .models import Album, RecordLabel, Artist


# Register your models here.
admin.site.register(Album)
admin.site.register(RecordLabel)
admin.site.register(Artist)