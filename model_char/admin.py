from django.contrib import admin
from model_char.models import Album,Song

# Register your models here.
@admin.register(Album)
class AlbumContent(admin.ModelAdmin):
    def __str__(self):
        pass

@admin.register(Song)
class SongContent(admin.ModelAdmin):
    pass    

#admin.site.register(Song) -- if we want to register and not want any filter 