from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    Usuario,
    Secretaria,
    Fornecedor,
    Contrato,
    Aditivo,
    Evento,
    Midia,
    ProducaoMidia,
    Veiculacao,
    ConferenciaMidiaDigital,
    Campanha,
    UsoCampanha,
    ClipagemAutomatica,
)

# Para mostrar campos customizados do seu modelo Usuario no admin
class CustomUserAdmin(UserAdmin):
    # Adiciona os campos 'perfil' e 'secretaria' na tela de edição do usuário
    fieldsets = UserAdmin.fieldsets + (
        ('Campos Personalizados', {'fields': ('perfil', 'secretaria')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Campos Personalizados', {'fields': ('perfil', 'secretaria')}),
    )

# --- Registrando cada um dos seus modelos ---
admin.site.register(Usuario, CustomUserAdmin)
admin.site.register(Secretaria)
admin.site.register(Fornecedor)
admin.site.register(Aditivo)
admin.site.register(Evento)
admin.site.register(Midia)
admin.site.register(ProducaoMidia)
admin.site.register(Veiculacao)
admin.site.register(ConferenciaMidiaDigital)
admin.site.register(Campanha)
admin.site.register(UsoCampanha)
admin.site.register(ClipagemAutomatica)