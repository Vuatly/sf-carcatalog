from django.contrib import admin
from .models import Car

@admin.register(Car)
class AdminCar(admin.ModelAdmin):
    pass

