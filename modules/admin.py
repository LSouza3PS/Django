# clientes/admin.py
from django.contrib import admin
from .models import Cliente, Fornecedor, Funcionario, OutroModulo

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('codigo', 'tipo_pessoa', 'cpf_cnpj', 'rg_ie', 'nome', 'sexo', 'carteira_trabalho', 'data_nascimento'),
        }),
        ('Informações de Contato', {
            'fields': ('telefone', 'telefone2', 'celular', 'email', 'fax'),
        }), 
        ('Endereço', {
            'fields': ('cep', 'rua_av', 'numero_rua_av', 'bairro', 'pais', 'uf', 'cidade_municipio', 'complemento'),
        }),
    )

    list_display = ['codigo', 'tipo_pessoa', 'cpf_cnpj', 'rg_ie', 'nome', 'sexo', 'carteira_trabalho', 'data_nascimento', 'telefone', 'telefone2', 'celular', 'email', 'fax', 'cep', 'rua_av', 'numero_rua_av', 'bairro', 'pais', 'uf', 'cidade_municipio', 'complemento']
    search_fields = ['codigo', 'nome', 'email']
    list_filter = ('tipo_pessoa', 'sexo', 'bairro', 'pais', 'uf', 'cidade_municipio')
    
admin.site.register(Fornecedor)
admin.site.register(Funcionario)
admin.site.register(OutroModulo)