# Django Base Project

Stack produtivo e reutilizável com Django 5, PostgreSQL, Docker e Nginx, incluindo admin moderno com Django Unfold e um app de configurações (ProjectConfig) para identidade e dados globais do projeto.

## 🔥 Destaques
- **Django 5.0.3** + **DRF** para APIs
- **Django Unfold** para um admin moderno
- **Auto-reload no navegador** com `django-browser-reload`
- **PostgreSQL 13** com volumes persistentes
- **Nginx** servindo `static/` e `media/` (produção)
- **Docker Compose** com ambientes dev e prod
- **App configs_project** com `ProjectConfig` (singleton) e `SocialLink`

## 📦 Estrutura
```
.
├── djangoapp/
│   ├── project/               # settings/urls/unfold_settings
│   ├── configs_project/       # models/admin/views/templates
│   ├── templates/             # overrides do admin
│   ├── manage.py
│   └── requirements.txt
├── data/web/{static,media}/   # volumes montados
├── nginx/nginx.conf           # reverse proxy (prod)
├── scripts/{entrypoint.sh,commands.sh}
├── docker-compose.dev.yml
├── docker-compose.prod.yml
├── Dockerfile
├── dotenv_files/.env-example
└── README.md
```

## ✅ Pré-requisitos
- Docker e Docker Compose
- Git

## ⚙️ Configuração
1) Copie o `.env` de exemplo e edite:
```bash
cp dotenv_files/.env-example .env
```
Variáveis essenciais:
```bash
SECRET_KEY="chave-secreta"
DEBUG="1"                     # 1 dev, 0 produção
ALLOWED_HOSTS="localhost,192.168.0.110"
CORS_ALLOWED_ORIGINS="http://localhost:8800"
CSRF_TRUSTED_ORIGINS="http://localhost:8800"
POSTGRES_DB="base_django"
POSTGRES_USER="base_django_user"
POSTGRES_PASSWORD="base_django_password"
```

## 🚀 Subir ambiente
Desenvolvimento:
```bash
docker compose -f docker-compose.dev.yml up --build
```
Produção (com Nginx):
```bash
docker compose -f docker-compose.prod.yml up -d --build
```

URLs:
- App: `http://localhost:8800`
- Admin: `http://localhost:8800/admin`

Superusuário padrão (criado por `scripts/commands.sh`):
- Usuário: `root`
- Senha: `231212`

## 🧩 App de Configurações (configs_project)
- `ProjectConfig` (singleton) armazena:
  - Nome, slogan, descrição
  - Logo, logo dark, favicon
  - E-mail, telefone, WhatsApp
  - Endereço completo + coordenadas
  - Redes sociais, horários, SEO
  - Scripts (GA, GTM, Pixel), modo manutenção
- `SocialLink` para links extras com ordenação e ícones.

Usar nos templates (contexto global via `get_project_config`):
```django
{{ project_config.project_name }}
{% if project_config.logo %}<img src="{{ project_config.logo.url }}" />{% endif %}
```

Home modular em `configs_project/templates/configs_project/`:
- `base.html`, `home.html`
- Componentes: `components/logo.html`, `gear_loader.html`, `info_cards.html`, `social_links.html`

## 🧑‍💻 Desenvolvimento mais rápido
`django-browser-reload` já está no `requirements.txt`.
Habilite nas URLs (apenas DEBUG):
```python
from django.conf import settings
from django.urls import path, include
if settings.DEBUG:
    urlpatterns += [path("__reload__/", include("django_browser_reload.urls"))]
```

## 📜 Comandos úteis
```bash
# Logs
docker compose logs -f djangoservice

# Migrações
docker compose exec djangoservice python manage.py makemigrations
docker compose exec djangoservice python manage.py migrate

# Coletar estáticos
docker compose exec djangoservice python manage.py collectstatic --no-input

# Shell
docker compose exec djangoservice python manage.py shell
```

## 🛡️ Produção – checklist
- `DEBUG="0"`
- `ALLOWED_HOSTS` e `CSRF_TRUSTED_ORIGINS` com schema (`https://`)
- Certificados SSL válidos
- `SECRET_KEY` única e segura
- Senhas fortes e backups do banco
- Logs e firewall configurados

## 🔧 Troubleshooting
- Erro ao servir mídia em dev: confira em `project/urls.py` se está usando `document_root=settings.MEDIA_ROOT`.
- CSRF/CORS em Django 4+: sempre use `http://` ou `https://` nas origens.
- Permissões de `static/` e `media/`: corrigidas por `entrypoint.sh` e `Dockerfile`.

## 📧 Email (Zoho exemplo)
```bash
EMAIL_HOST="smtp.zoho.com"
EMAIL_PORT="587"
EMAIL_USE_TLS="1"
EMAIL_HOST_USER="seu-email@zoho.com"
EMAIL_HOST_PASSWORD="sua-senha-app"
DEFAULT_FROM_EMAIL="seu-email@zoho.com"
```

## 📄 Licença
MIT.

—
Mantido por Estrutura Córtex • PantojaVII


