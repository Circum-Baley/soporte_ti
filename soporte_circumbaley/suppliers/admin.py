from django.contrib import admin
from .models import Supplier


# Register your models here.
class SuppliersAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']

    class Media:
        css = {
            'all': ('supplies/css/custom_ckeditor.css',)
        }


admin.site.register(Supplier, SuppliersAdmin)
