from django.contrib import admin
from . models import Courses, Category
# Register your models here.

@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ("name", "available")
    list_filter = ("available", )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields= {
        "slug":("name", )
    }
