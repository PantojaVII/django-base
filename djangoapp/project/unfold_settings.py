import os

# Context processor para obter a logo dinamicamente
def get_logo_url(request):
    from configs_project.models import ProjectConfig
    try:
        config = ProjectConfig.get_config()
        if config.logo:
            return config.logo.url
    except:
        pass
    return None

# Configuração do Django Unfold
UNFOLD = {
    "SITE_TITLE": None,  # Será definido dinamicamente
    "SITE_HEADER": None,  # Será definido dinamicamente
    "SITE_URL": "/",
    
    # Logo customizada
    "SITE_LOGO": {
        "light": get_logo_url,  # Função que retorna URL da logo
        "dark": get_logo_url,   # Pode usar logo_dark se preferir
    },
    
    # Ícone padrão (fallback caso não tenha logo)
    "SITE_ICON": {
        "light": lambda request: "dashboard",
        "dark": lambda request: "dashboard",
    },
    
    "SITE_SYMBOL": "dashboard",  # Símbolo exibido quando não há logo
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,
    
    "ENVIRONMENT": "development",
    
    "COLORS": {
        "primary": {
            "50": "239 246 255",
            "100": "219 234 254", 
            "200": "191 219 254",
            "300": "147 197 253",
            "400": "96 165 250",
            "500": "59 130 246",
            "600": "37 99 235",
            "700": "29 78 216",
            "800": "30 64 175",
            "900": "30 58 138",
            "950": "23 37 84",
        },
    },
    
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": True,
        "navigation": [
            {
                "title": "Dashboard",
                "separator": True,
                "items": [
                    {
                        "title": "Home",
                        "icon": "home",
                        "link": "/admin/",
                    },
                ],
            },
            {
                "title": "Gerenciamento",
                "separator": True,
                "items": [
                    {
                        "title": "Usuários",
                        "icon": "people",
                        "link": "/admin/auth/user/",
                    },
                    {
                        "title": "Grupos",
                        "icon": "group",
                        "link": "/admin/auth/group/",
                    },
                ],
            },
            {
                "title": "Configurações",
                "separator": True,
                "items": [
                    {
                        "title": "Configuração do Projeto",
                        "icon": "settings",
                        "link": "/admin/configs_project/projectconfig/",
                    },
                ],
            },
        ],
    },
}
