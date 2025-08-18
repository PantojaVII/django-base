from django.contrib import admin
from ..models import Aditivo

@admin.register(Aditivo)
class AditivoAdmin(admin.ModelAdmin):
    list_display = ('contrato', 'descricao', 'data', 'valor')
    search_fields = ('contrato',)
    list_filter = ('data', 'valor')