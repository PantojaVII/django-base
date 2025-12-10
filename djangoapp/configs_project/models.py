from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError


class ProjectConfig(models.Model):
    """
    Configurações globais do projeto.
    Implementa o padrão Singleton - apenas uma instância pode existir.
    """
    
    # Identidade do Projeto
    project_name = models.CharField(
        'Nome do Projeto',
        max_length=200,
        default='Meu Projeto',
        help_text='Nome que aparecerá no site e admin'
    )
    
    project_slogan = models.CharField(
        'Slogan',
        max_length=255,
        blank=True,
        help_text='Slogan ou tagline do projeto'
    )
    
    project_description = models.TextField(
        'Descrição',
        blank=True,
        help_text='Descrição detalhada do projeto'
    )
    
    # Logos e Ícones
    logo = models.ImageField(
        'Logo Principal',
        upload_to='config/logos/',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg', 'svg', 'webp'])],
        help_text='Logo principal do projeto (recomendado: 300x100px)'
    )
    
    logo_dark = models.ImageField(
        'Logo Modo Escuro',
        upload_to='config/logos/',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg', 'svg', 'webp'])],
        help_text='Logo para modo escuro (opcional)'
    )
    
    favicon = models.ImageField(
        'Favicon',
        upload_to='config/icons/',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(['ico', 'png'])],
        help_text='Ícone do site (recomendado: 32x32px ou 16x16px)'
    )
    
    # Informações de Contato
    email = models.EmailField(
        'E-mail Principal',
        blank=True,
        help_text='E-mail principal para contato'
    )
    
    phone = models.CharField(
        'Telefone',
        max_length=20,
        blank=True,
        help_text='Telefone para contato (ex: +55 11 99999-9999)'
    )
    
    whatsapp = models.CharField(
        'WhatsApp',
        max_length=20,
        blank=True,
        help_text='Número do WhatsApp (ex: +5511999999999)'
    )
    
    # Endereço
    address_street = models.CharField(
        'Logradouro',
        max_length=255,
        blank=True,
        help_text='Rua, avenida, etc.'
    )
    
    address_number = models.CharField(
        'Número',
        max_length=20,
        blank=True
    )
    
    address_complement = models.CharField(
        'Complemento',
        max_length=100,
        blank=True,
        help_text='Apartamento, sala, bloco, etc.'
    )
    
    address_neighborhood = models.CharField(
        'Bairro',
        max_length=100,
        blank=True
    )
    
    address_city = models.CharField(
        'Cidade',
        max_length=100,
        blank=True
    )
    
    address_state = models.CharField(
        'Estado',
        max_length=2,
        blank=True,
        help_text='Sigla do estado (ex: SP, RJ)'
    )
    
    address_zipcode = models.CharField(
        'CEP',
        max_length=9,
        blank=True,
        help_text='Formato: 00000-000'
    )
    
    address_country = models.CharField(
        'País',
        max_length=100,
        default='Brasil'
    )
    
    # Coordenadas para Mapa
    latitude = models.DecimalField(
        'Latitude',
        max_digits=10,
        decimal_places=7,
        blank=True,
        null=True,
        help_text='Coordenada de latitude para mapa'
    )
    
    longitude = models.DecimalField(
        'Longitude',
        max_digits=10,
        decimal_places=7,
        blank=True,
        null=True,
        help_text='Coordenada de longitude para mapa'
    )
    
    # Redes Sociais
    facebook_url = models.URLField('Facebook', blank=True, max_length=255)
    instagram_url = models.URLField('Instagram', blank=True, max_length=255)
    twitter_url = models.URLField('Twitter/X', blank=True, max_length=255)
    linkedin_url = models.URLField('LinkedIn', blank=True, max_length=255)
    youtube_url = models.URLField('YouTube', blank=True, max_length=255)
    tiktok_url = models.URLField('TikTok', blank=True, max_length=255)
    
    # Horários de Funcionamento
    business_hours = models.TextField(
        'Horário de Funcionamento',
        blank=True,
        help_text='Ex: Seg-Sex: 9h às 18h | Sáb: 9h às 13h'
    )
    
    # SEO e Metadados
    meta_keywords = models.CharField(
        'Palavras-chave (SEO)',
        max_length=255,
        blank=True,
        help_text='Palavras-chave separadas por vírgula'
    )
    
    meta_description = models.CharField(
        'Meta Descrição (SEO)',
        max_length=160,
        blank=True,
        help_text='Descrição que aparece nos resultados de busca (máx. 160 caracteres)'
    )
    
    # Scripts Personalizados
    google_analytics_id = models.CharField(
        'Google Analytics ID',
        max_length=50,
        blank=True,
        help_text='Ex: G-XXXXXXXXXX'
    )
    
    google_tag_manager_id = models.CharField(
        'Google Tag Manager ID',
        max_length=50,
        blank=True,
        help_text='Ex: GTM-XXXXXXX'
    )
    
    facebook_pixel_id = models.CharField(
        'Facebook Pixel ID',
        max_length=50,
        blank=True
    )
    
    custom_head_scripts = models.TextField(
        'Scripts Personalizados (HEAD)',
        blank=True,
        help_text='Scripts que serão inseridos no <head>'
    )
    
    custom_body_scripts = models.TextField(
        'Scripts Personalizados (BODY)',
        blank=True,
        help_text='Scripts que serão inseridos antes do </body>'
    )
    
    # Status
    is_active = models.BooleanField(
        'Ativo',
        default=True,
        help_text='Define se as configurações estão ativas'
    )
    
    maintenance_mode = models.BooleanField(
        'Modo Manutenção',
        default=False,
        help_text='Ativa o modo de manutenção do site'
    )
    
    maintenance_message = models.TextField(
        'Mensagem de Manutenção',
        blank=True,
        default='Estamos em manutenção. Voltaremos em breve!',
        help_text='Mensagem exibida quando o site está em manutenção'
    )
    
    # Metadados do Sistema
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    
    class Meta:
        verbose_name = 'Configuração do Projeto'
        verbose_name_plural = 'Configurações do Projeto'
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.project_name}'
    
    def save(self, *args, **kwargs):
        """
        Garante que apenas uma instância de configuração existe (Singleton).
        """
        if not self.pk and ProjectConfig.objects.exists():
            raise ValidationError('Já existe uma configuração. Edite a configuração existente.')
        return super().save(*args, **kwargs)
    
    def get_full_address(self):
        """Retorna o endereço completo formatado."""
        parts = []
        
        if self.address_street:
            street_part = self.address_street
            if self.address_number:
                street_part += f', {self.address_number}'
            if self.address_complement:
                street_part += f' - {self.address_complement}'
            parts.append(street_part)
        
        if self.address_neighborhood:
            parts.append(self.address_neighborhood)
        
        if self.address_city:
            city_part = self.address_city
            if self.address_state:
                city_part += f' - {self.address_state}'
            parts.append(city_part)
        
        if self.address_zipcode:
            parts.append(f'CEP: {self.address_zipcode}')
        
        return ', '.join(parts) if parts else ''
    
    @classmethod
    def get_config(cls):
        """
        Retorna a configuração ativa ou cria uma nova se não existir.
        """
        config, created = cls.objects.get_or_create(pk=1)
        return config


class SocialLink(models.Model):
    """
    Links de redes sociais adicionais e personalizados.
    """
    PLATFORM_CHOICES = [
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('twitter', 'Twitter/X'),
        ('linkedin', 'LinkedIn'),
        ('youtube', 'YouTube'),
        ('tiktok', 'TikTok'),
        ('pinterest', 'Pinterest'),
        ('github', 'GitHub'),
        ('behance', 'Behance'),
        ('dribbble', 'Dribbble'),
        ('medium', 'Medium'),
        ('telegram', 'Telegram'),
        ('discord', 'Discord'),
        ('twitch', 'Twitch'),
        ('spotify', 'Spotify'),
        ('other', 'Outro'),
    ]
    
    project_config = models.ForeignKey(
        ProjectConfig,
        on_delete=models.CASCADE,
        related_name='social_links',
        verbose_name='Configuração'
    )
    
    platform = models.CharField(
        'Plataforma',
        max_length=50,
        choices=PLATFORM_CHOICES
    )
    
    custom_name = models.CharField(
        'Nome Customizado',
        max_length=100,
        blank=True,
        help_text='Use apenas se escolher "Outro"'
    )
    
    url = models.URLField('URL', max_length=255)
    
    icon_class = models.CharField(
        'Classe do Ícone',
        max_length=100,
        blank=True,
        help_text='Ex: fab fa-facebook (Font Awesome)'
    )
    
    is_active = models.BooleanField('Ativo', default=True)
    order = models.PositiveIntegerField('Ordem', default=0)
    
    class Meta:
        verbose_name = 'Link de Rede Social'
        verbose_name_plural = 'Links de Redes Sociais'
        ordering = ['order', 'platform']
    
    def __str__(self):
        name = self.custom_name if self.platform == 'other' else self.get_platform_display()
        return f'{name} - {self.url}'
