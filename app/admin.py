from django.contrib import admin
from .models import *


class MovieAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']


admin.site.register(Movie, MovieAdmin)
admin.site.register(Ticket)
admin.site.register(Place)
