from django.contrib import admin
from ..models import Veiculacao

@admin.register(Veiculacao)
class VeiculacaoAdmin(admin.ModelAdmin):
    list_display = ('producao', 'midia', 'data_inicio', 'data_fim')
    search_fields = ('producao', 'midia', 'data_inicio', 'data_fim')
    list_filter = ('producao', 'data_inicio', 'data_fim')