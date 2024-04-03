from django.contrib import admin
from .models import Cliente, Servico, SolicitacaoServico, ItemSolicitacao, OutroModulo

# Registro dos modelos
class ClienteAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('tipo_pessoa', 'cpf_cnpj', 'rg_ie', 'nome', 'sexo', 'carteira_trabalho', 'data_nascimento'),
        }),
        ('Informações de Contato', {
            'fields': ('celular', 'email', 'telefone', 'telefone2', 'fax'),
        }), 
        ('Endereço', {
            'fields': ('rua_av', 'numero_rua_av', 'complemento', 'bairro', 'pais', 'uf', 'cidade_municipio', 'cep'),
        }),
    )
    list_display = ['codigo', 'tipo_pessoa', 'cpf_cnpj', 'rg_ie', 'nome', 'sexo', 'carteira_trabalho', 'data_nascimento', 'telefone', 'telefone2', 'celular', 'email', 'fax', 'cep', 'rua_av', 'numero_rua_av', 'bairro', 'pais', 'uf', 'cidade_municipio', 'complemento']
    search_fields = ['codigo', 'nome', 'email']
    list_filter = ('tipo_pessoa', 'sexo', 'bairro', 'pais', 'uf', 'cidade_municipio')

class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ['nome']

class ItemSolicitacaoInline(admin.TabularInline):
    model = ItemSolicitacao
    extra = 1

class SolicitacaoServicoAdmin(admin.ModelAdmin):
    inlines = [ItemSolicitacaoInline]
    list_display = ('cliente', 'servico', 'status', 'data_entrega', 'data_solicitacao')
    list_filter = ('status', 'data_solicitacao', 'data_entrega')
    search_fields = ['cliente__username', 'servico__nome']

class OutroModuloAdmin(admin.ModelAdmin):
    pass

# Registro dos modelos
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Servico, ServicoAdmin)
admin.site.register(SolicitacaoServico, SolicitacaoServicoAdmin)
admin.site.register(OutroModulo, OutroModuloAdmin)