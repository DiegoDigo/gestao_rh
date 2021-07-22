from django.contrib import admin
from .models import RegisteroHoraExtra


@admin.register(RegisteroHoraExtra)
class RegistroHoraExtraAdmin(admin.ModelAdmin):
    list_display = ('motivo',)
