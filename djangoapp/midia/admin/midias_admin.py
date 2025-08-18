from django.contrib import admin
from ..models import Midia

@admin.register(Midia)
class MidiaAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'formato', 'descricao')
    search_fields = ('tipo', 'descricao')
    list_filter = ('tipo', 'formato')