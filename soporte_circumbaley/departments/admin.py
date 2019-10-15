from django.contrib import admin
from .models import Department


# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']

    class Media:
        css = {
            'all': ('departments/css/custom_ckeditor.css',)
        }


admin.site.register(Department, DepartmentAdmin)
