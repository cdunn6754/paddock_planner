from django.contrib import admin
from horses.models import Horse


class HorseAdmin(admin.ModelAdmin):
    pass


admin.site.register(Horse, HorseAdmin)
