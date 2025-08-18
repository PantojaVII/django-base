from django.contrib import admin
from ..models import Fornecedor

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('nome_razao_social', 'cnpj', 'tipo')
    search_fields = ('nome_razao_social', 'cnpj', 'tipo')
    list_filter = ('nome_razao_social',)