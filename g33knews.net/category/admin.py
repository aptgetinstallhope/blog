from django.contrib import admin
from .models import MainCategories

class MainCategoriesAdmin(admin.ModelAdmin):
    list_display = ['id' , 'categoryengname' , 'categorypersianname' , 'active']
admin.site.register(MainCategories , MainCategoriesAdmin)
