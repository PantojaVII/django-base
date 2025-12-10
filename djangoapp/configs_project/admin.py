from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.decorators import display
from .models import ProjectConfig, SocialLink


class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 1
    fields = ('platform', 'custom_name', 'url', 'icon_class', 'is_active', 'order')


@admin.register(ProjectConfig)
class ProjectConfigAdmin(ModelAdmin):
    inlines = [SocialLinkInline]
    
    fieldsets = (
        ('🏢 Identidade do Projeto', {
            'fields': ('project_name', 'project_slogan', 'project_description')
        }),
        ('🎨 Logos e Ícones', {
            'fields': ('logo', 'logo_dark', 'favicon'),
            'classes': ('collapse',)
        }),
        ('📞 Informações de Contato', {
            'fields': ('email', 'phone', 'whatsapp')
        }),
        ('📍 Endereço', {
            'fields': (
                'address_street', 'address_number', 'address_complement',
                'address_neighborhood', 'address_city', 'address_state',
                'address_zipcode', 'address_country',
                ('latitude', 'longitude')
            ),
            'classes': ('collapse',)
        }),
        ('🌐 Redes Sociais Principais', {
            'fields': (
                'facebook_url', 'instagram_url', 'twitter_url',
                'linkedin_url', 'youtube_url', 'tiktok_url'
            ),
            'classes': ('collapse',)
        }),
        ('⏰ Horários', {
            'fields': ('business_hours',),
            'classes': ('collapse',)
        }),
        ('🔍 SEO e Metadados', {
            'fields': ('meta_keywords', 'meta_description'),
            'classes': ('collapse',)
        }),
        ('📊 Scripts e Rastreamento', {
            'fields': (
                'google_analytics_id', 'google_tag_manager_id',
                'facebook_pixel_id', 'custom_head_scripts', 'custom_body_scripts'
            ),
            'classes': ('collapse',)
        }),
        ('⚙️ Status do Sistema', {
            'fields': ('is_active', 'maintenance_mode', 'maintenance_message')
        }),
        ('📅 Informações do Sistema', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ('created_at', 'updated_at')
    
    list_display = ('project_name', 'email', 'is_active_display', 'maintenance_mode_display', 'updated_at')
    list_filter = ('is_active', 'maintenance_mode', 'created_at', 'updated_at')
    search_fields = ('project_name', 'project_slogan', 'email', 'phone')
    
    @display(description='Status', boolean=True)
    def is_active_display(self, obj):
        return obj.is_active
    
    @display(description='Manutenção', boolean=True)
    def maintenance_mode_display(self, obj):
        return obj.maintenance_mode
    
    def has_add_permission(self, request):
        """Permite adicionar apenas se não existir configuração."""
        return not ProjectConfig.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        """Não permite deletar a configuração."""
        return False


@admin.register(SocialLink)
class SocialLinkAdmin(ModelAdmin):
    list_display = ('platform', 'custom_name', 'url_short', 'is_active', 'order')
    list_filter = ('platform', 'is_active')
    search_fields = ('custom_name', 'url')
    list_editable = ('is_active', 'order')
    ordering = ('order', 'platform')
    
    fieldsets = (
        (None, {
            'fields': ('project_config', 'platform', 'custom_name', 'url', 'icon_class')
        }),
        ('Configurações', {
            'fields': ('is_active', 'order')
        }),
    )
    
    @display(description='URL')
    def url_short(self, obj):
        return obj.url[:50] + '...' if len(obj.url) > 50 else obj.url
