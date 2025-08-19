from django.contrib import admin
from ..models import Campanha, UsoCampanha

# (Boa Prática) Inline para gerenciar a relação ManyToMany com ProducaoMidia
# Isso permite adicionar/remover produções diretamente na tela da campanha.
class UsoCampanhaInline(admin.TabularInline):
    model = UsoCampanha
    # 'extra=1' significa que sempre haverá um campo extra para adicionar uma nova produção.
    extra = 1
    # Melhora a performance carregando os nomes de produção de forma mais eficiente.
    raw_id_fields = ('producao',)

@admin.register(Campanha)
class CampanhaAdmin(admin.ModelAdmin):
    # Campos que serão exibidos na lista de campanhas.
    list_display = ('nome', 'data_inicio', 'data_fim')
    
    # Campos pelos quais você poderá pesquisar.
    search_fields = ('nome', 'objetivo')
    
    # Filtros que aparecerão na barra lateral direita.
    list_filter = ('data_inicio', 'data_fim')
    
    # Adiciona o gerenciador inline criado acima na tela de edição da campanha.
    inlines = (UsoCampanhaInline,)