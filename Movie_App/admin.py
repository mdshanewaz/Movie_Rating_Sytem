from django.contrib import admin
from Movie_App.models import GenreModel, MovieModel, RateModel

# Register your models here.
admin.site.register(GenreModel)
admin.site.register(RateModel)
admin.site.register(MovieModel)