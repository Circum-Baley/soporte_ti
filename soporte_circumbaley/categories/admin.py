from django.contrib import admin
from .models import Category


# Register your models here.
class CategoriesAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']

    class Media:
        css = {
            'all': ('categories/css/custom_ckeditor.css',)
        }


admin.site.register(Category, CategoriesAdmin)
