from django.contrib import admin
from .models import Events, Location


# added line
# Register your models here.

admin.site.register(Events)
admin.site.register(Location)
