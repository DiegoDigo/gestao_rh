from django.contrib import admin
from .models import Documentos


@admin.register(Documentos)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
