from django.contrib import admin
from .models import Album, Song, Customer,Podcasts
# Register your models here.

admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Customer)
admin.site.register(Podcasts)