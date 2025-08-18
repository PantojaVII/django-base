from django.contrib import admin
from ..models import ProducaoMidia

@admin.register(ProducaoMidia)
class ProducaoMidiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_producao', 'fornecedor', 'evento')
    search_fields = ('titulo', 'data_producao', 'fornecedor', 'evento')
    list_filter = ('titulo', 'data_producao',)