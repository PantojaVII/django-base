from django.contrib import admin
from ..models import Evento

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('contrato', 'nome', 'data_inicio', 'data_fim')
    search_fields = ('contrato', 'nome')
    list_filter = ('data_inicio',)