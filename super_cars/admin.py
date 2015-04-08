from django.contrib import admin
from .models import Car, Manufacturer
# Register your models here.

class ManufacturerAdmin(admin.ModelAdmin):
        fields = ['name']

class CarAdmin(admin.ModelAdmin):
        fields = ['name', 'manufacturer']

admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Car, CarAdmin)
