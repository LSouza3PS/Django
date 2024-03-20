from django.db import models
from django.utils import timezone

UF_CHOICES = [
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
]

# Create your models here.
class Cliente(models.Model):
    codigo = models.CharField(max_length=20, unique=True, verbose_name='Código')
    tipo_pessoa = models.CharField(max_length=1, choices=[('F', 'Física'), ('J', 'Jurídica')], verbose_name='Tipo de Pessoa')
    cpf_cnpj = models.CharField(max_length=18, unique=True, verbose_name='CPF/CNPJ')
    rg_ie = models.CharField(max_length=15, blank=True, null=True, verbose_name='RG/IE')
    nome = models.CharField(max_length=100, verbose_name='Nome')
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], verbose_name='Sexo')
    carteira_trabalho = models.CharField(max_length=20, blank=True, null=True, verbose_name='Carteira de Trabalho')
    data_nascimento = models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')
    insc_municipal = models.CharField(max_length=20, blank=True, null=True, verbose_name='Inscrição Municipal')
    razao_social = models.CharField(max_length=100, blank=True, null=True, verbose_name='Razão Social')
    cep = models.CharField(max_length=10, verbose_name='CEP')
    rua_av = models.CharField(max_length=255, verbose_name='Rua/Avenida')
    numero_rua_av = models.CharField(max_length=10, verbose_name='Número')
    bairro = models.CharField(max_length=100, verbose_name='Bairro')
    pais = models.CharField(max_length=50, verbose_name='País')
    uf = models.CharField(max_length=2, choices=UF_CHOICES, verbose_name='UF')
    cidade_municipio = models.CharField(max_length=100, verbose_name='Cidade/Município')
    complemento = models.CharField(max_length=255, blank=True, null=True, verbose_name='Complemento')
    telefone = models.CharField(max_length=15, blank=True, null=True, verbose_name='Telefone')
    telefone2 = models.CharField(max_length=15, blank=True, null=True, verbose_name='Telefone 2')
    celular = models.CharField(max_length=15, blank=True, null=True, verbose_name='Celular')
    email = models.EmailField(unique=True, verbose_name='E-mail')
    fax = models.CharField(max_length=15, blank=True, null=True, verbose_name='Fax')
    

    def __str__(self):
        return f"{self.codigo} - {self.nome}"
    
    
    class Meta:
        verbose_name = 'Cliente'

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Serviço"

class SolicitacaoServico(models.Model):
    STATUS_CHOICES = (
        ('Pendente', 'Pendente'),
        ('Em Andamento', 'Em Andamento'),
        ('Concluído', 'Concluído'),
        ('Cancelado', 'Cancelado'),
    )

    cliente = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pendente')
    data_solicitacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Solicitação de {self.servico.nome} por {self.cliente.username}"
    
    class Meta:
        verbose_name = "Solicitação de Serviço"
        verbose_name_plural = "Solicitações de Serviço"

class ItemSolicitacao(models.Model):
    solicitacao = models.ForeignKey(SolicitacaoServico, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def total(self):
        return self.quantidade * self.preco_unitario

    def __str__(self):
        return f"{self.quantidade} x {self.solicitacao.servico.nome}"
        
class OutroModulo(models.Model):
    codigo = models.CharField(max_length=20, unique=True, verbose_name='Código')
    
    class Meta:
        verbose_name = 'Outro Módulo...'
        verbose_name_plural = 'Outros Módulos...'