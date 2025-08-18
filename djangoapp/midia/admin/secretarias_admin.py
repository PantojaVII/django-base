from django.contrib import admin
from ..models import Secretaria

@admin.register(Secretaria)
class SecretariaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla')
    search_fields = ('nome', 'sigla')
    list_filter = ('nome',)