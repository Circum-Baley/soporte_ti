from django.contrib import admin
from .models import Service


# Register your models here.
class ServicesAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']

    class Media:
        css = {
            'all': ('devices/css/custom_ckeditor.css',)
        }


admin.site.register(Service, ServicesAdmin)
