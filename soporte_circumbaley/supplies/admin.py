from django.contrib import admin
from .models import Supply


# Register your models here.
class SuppliesAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']

    class Media:
        css = {
            'all': ('supplies/css/custom_ckeditor.css',)
        }


admin.site.register(Supply, SuppliesAdmin)
