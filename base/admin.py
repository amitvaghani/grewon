from django.contrib import admin
from .models import User,Event
from django.conf import settings


class USerAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name')
admin.site.register(User, USerAdmin)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title","start","end","latitude","longitude")
