from django.contrib import admin
from model_char.models import Album,Song,Author,Book,Vehicle,Car

# Register your models here.
@admin.register(Album)
class AlbumContent(admin.ModelAdmin):
    def __str__(self):
        pass

@admin.register(Song)
class SongContent(admin.ModelAdmin):
    pass    

#admin.site.register(Song) -- if we want to register and not want any filter 


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Vehicle)
admin.site.register(Car)