from django.contrib import admin
from ..models import Contrato

@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ('numero_contrato', 'secretaria', 'data_inicio', 'data_fim')
    search_fields = ('secretaria',)
    list_filter = ('data_inicio', 'data_fim')