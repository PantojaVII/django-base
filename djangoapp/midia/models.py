from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Usuario(AbstractUser):
    perfil = models.CharField(max_length=100, blank=True, null=True, help_text="Ex: Administrador, Usuário Padrão")
    secretaria = models.ForeignKey(
        'Secretaria',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='usuarios'
    )

    # --- ADICIONE ESTAS DUAS SEÇÕES PARA RESOLVER O CONFLITO ---
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name="usuario_set",  # Nome de acesso reverso único
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="usuario_permissions_set", # Nome de acesso reverso único
        related_query_name="user",
    )
    
    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

class Secretaria(models.Model):
    nome = models.CharField(max_length=255)
    sigla = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.sigla} - {self.nome}"
    class Meta:
        verbose_name = "Secretaria"
        verbose_name_plural = "Secretarias"

class Fornecedor(models.Model):
    nome_razao_social = models.CharField(max_length=255, verbose_name="Nome/Razão Social")
    cnpj = models.CharField(max_length=18, unique=True)
    tipo = models.CharField(max_length=100)
    certidoes_anexadas = models.FileField(upload_to='certidoes/', blank=True, null=True, verbose_name="Certidões Anexadas")
    def __str__(self):
        return self.nome_razao_social
    class Meta:
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"

class Contrato(models.Model):
    secretaria = models.ForeignKey(Secretaria, on_delete=models.PROTECT, related_name='contratos')
    numero_contrato = models.CharField(max_length=100, unique=True, verbose_name="Número do Contrato")
    objeto = models.TextField()
    data_inicio = models.DateField(verbose_name="Data de Início")
    data_fim = models.DateField(verbose_name="Data de Fim")
    valor_total = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Valor Total")
    situacao = models.CharField(max_length=100, verbose_name="Situação")
    tipo_contrato = models.CharField(max_length=100, verbose_name="Tipo de Contrato")
    def __str__(self):
        return f"Contrato nº {self.numero_contrato}"
    class Meta:
        verbose_name = "Contrato"
        verbose_name_plural = "Contratos"

class Aditivo(models.Model):
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE, related_name='aditivos')
    descricao = models.TextField(verbose_name="Descrição")
    data = models.DateField()
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    def __str__(self):
        return f"Aditivo para {self.contrato} - {self.data}"
    class Meta:
        verbose_name = "Aditivo"
        verbose_name_plural = "Aditivos"

class Evento(models.Model):
    contrato = models.ForeignKey(Contrato, on_delete=models.PROTECT, related_name='eventos')
    nome = models.CharField(max_length=255)
    data_inicio = models.DateField(verbose_name="Data de Início")
    data_fim = models.DateField(verbose_name="Data de Fim")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

class Midia(models.Model):
    TIPO_CHOICES = [('RADIO', 'Rádio'), ('TV', 'TV'), ('WEB', 'Web')]
    tipo = models.CharField(max_length=5, choices=TIPO_CHOICES)
    formato = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    def __str__(self):
        return f"{self.get_tipo_display()} - {self.formato}"
    class Meta:
        verbose_name = "Mídia"
        verbose_name_plural = "Mídias"

class ProducaoMidia(models.Model):
    titulo = models.CharField(max_length=255, verbose_name="Título")
    data_producao = models.DateField(verbose_name="Data de Produção")
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT, related_name='producoes')
    evento = models.ForeignKey(Evento, on_delete=models.PROTECT, related_name='producoes', blank=True, null=True)
    def __str__(self):
        return self.titulo
    class Meta:
        verbose_name = "Produção de Mídia"
        verbose_name_plural = "Produções de Mídia"

class Veiculacao(models.Model):
    producao = models.ForeignKey(ProducaoMidia, on_delete=models.CASCADE, related_name='veiculacoes')
    midia = models.ForeignKey(Midia, on_delete=models.PROTECT, related_name='veiculacoes')
    data_inicio = models.DateField(verbose_name="Data de Início")
    data_fim = models.DateField(verbose_name="Data de Fim")
    def __str__(self):
        return f"Veiculação de '{self.producao.titulo}' em '{self.midia}'"
    class Meta:
        verbose_name = "Veiculação"
        verbose_name_plural = "Veiculações"

class ConferenciaMidiaDigital(models.Model):
    STATUS_CHOICES = [('CONFIRMADO', 'Confirmado'), ('NAO_ENCONTRADO', 'Não encontrado')]
    producao = models.ForeignKey(ProducaoMidia, on_delete=models.CASCADE, related_name='conferencias')
    url_veiculo = models.URLField(max_length=500, verbose_name="URL do Veículo")
    data_verificacao = models.DateTimeField(auto_now_add=True, verbose_name="Data da Verificação")
    hash_encontrado = models.CharField(max_length=255, blank=True, null=True)
    status_verificacao = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name="Status")
    def __str__(self):
        return f"Conferência para '{self.producao.titulo}' - {self.status_verificacao}"
    class Meta:
        verbose_name = "Conferência de Mídia Digital"
        verbose_name_plural = "Conferências de Mídia Digital"

class Campanha(models.Model):
    nome = models.CharField(max_length=255)
    data_inicio = models.DateField(verbose_name="Data de Início")
    data_fim = models.DateField(verbose_name="Data de Fim")
    objetivo = models.TextField()
    producoes = models.ManyToManyField(ProducaoMidia, through='UsoCampanha', related_name='campanhas')
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Campanha"
        verbose_name_plural = "Campanhas"

class UsoCampanha(models.Model):
    campanha = models.ForeignKey(Campanha, on_delete=models.CASCADE)
    producao = models.ForeignKey(ProducaoMidia, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Uso em Campanha"
        verbose_name_plural = "Usos em Campanha"
        unique_together = ('campanha', 'producao')
    def __str__(self):
        return f"'{self.producao.titulo}' usado em '{self.campanha.nome}'"

class ClipagemAutomatica(models.Model):
    TIPO_MIDIA_CHOICES = [('BLOG', 'Blog'), ('REDESOCIAL', 'Rede Social'), ('SITE', 'Site')]
    campanha = models.ForeignKey(Campanha, on_delete=models.CASCADE, related_name='clipagens')
    palavra_chave = models.CharField(max_length=255, verbose_name="Palavra-chave")
    fonte = models.CharField(max_length=255)
    url = models.URLField(max_length=500)
    data_coleta = models.DateTimeField(auto_now_add=True, verbose_name="Data da Coleta")
    tipo_midia = models.CharField(max_length=20, choices=TIPO_MIDIA_CHOICES, verbose_name="Tipo de Mídia")
    conteudo_html = models.TextField(blank=True, null=True, verbose_name="Conteúdo HTML")
    imagem_salva = models.ImageField(upload_to='clipagens/', blank=True, null=True, verbose_name="Imagem Salva")
    def __str__(self):
        return f"Clipagem de '{self.palavra_chave}' em '{self.fonte}'"
    class Meta:
        verbose_name = "Clipagem Automática"
        verbose_name_plural = "Clipagens Automáticas"