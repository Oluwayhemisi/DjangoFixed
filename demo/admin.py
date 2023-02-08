from django.contrib import admin

# Register your models here.
from .models import House, Room

house = House.objects.create(name='_4000')
Room.objects.create(house=house)


class HouseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


class RoomAdmin(admin.ModelAdmin):
    list_display = ('pk', 'house')


admin.site.register(House, HouseAdmin)
admin.site.register(Room, RoomAdmin)
