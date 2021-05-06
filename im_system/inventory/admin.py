from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Order,Employee,Laptop,Mobile,Tab,Sim,Other)
class viewAdmin(admin.ModelAdmin):
    pass
