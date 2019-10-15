from django.contrib import admin
from .models import Document


# Register your models here.
class DocuemtsAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']

    class Media:
        css = {
            'all': ('documents/css/custom_ckeditor.css',)
        }


admin.site.register(Document, DocuemtsAdmin)
