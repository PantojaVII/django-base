from django.shortcuts import render
from .models import ProjectConfig


def home_view(request):
    """View da página inicial."""
    config = ProjectConfig.get_config()
    
    context = {
        'config': config,
        'page_title': 'Início',
    }
    
    return render(request, 'configs_project/home.html', context)


def get_project_config(request):
    """
    Context processor para disponibilizar as configurações em todos os templates.
    """
    config = ProjectConfig.get_config()
    return {
        'project_config': config
    }


def unfold_settings(request):
    """
    Context processor para Unfold - atualiza título e header dinamicamente.
    """
    from .models import ProjectConfig
    
    try:
        config = ProjectConfig.get_config()
        site_title = config.project_name or "Admin"
        site_header = config.project_slogan or "Painel Administrativo"
    except:
        site_title = "Admin"
        site_header = "Painel Administrativo"
    
    return {
        'UNFOLD_SITE_TITLE': site_title,
        'UNFOLD_SITE_HEADER': site_header,
    }
