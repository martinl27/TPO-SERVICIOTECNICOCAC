from django.contrib import admin
from .models import Carrito
# Register your models here.

class CarritoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Carrito, CarritoAdmin)