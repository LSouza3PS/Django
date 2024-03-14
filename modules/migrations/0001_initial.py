# Generated by Django 5.0.3 on 2024-03-14 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20, unique=True, verbose_name='Código')),
                ('tipo_pessoa', models.CharField(choices=[('F', 'Física'), ('J', 'Jurídica')], max_length=1, verbose_name='Tipo de Pessoa')),
                ('cpf_cnpj', models.CharField(max_length=18, unique=True, verbose_name='CPF/CNPJ')),
                ('rg_ie', models.CharField(blank=True, max_length=15, null=True, verbose_name='RG/IE')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], max_length=1, verbose_name='Sexo')),
                ('carteira_trabalho', models.CharField(blank=True, max_length=20, null=True, verbose_name='Carteira de Trabalho')),
                ('data_nascimento', models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')),
                ('insc_municipal', models.CharField(blank=True, max_length=20, null=True, verbose_name='Inscrição Municipal')),
                ('razao_social', models.CharField(blank=True, max_length=100, null=True, verbose_name='Razão Social')),
                ('cep', models.CharField(max_length=10, verbose_name='CEP')),
                ('rua_av', models.CharField(max_length=255, verbose_name='Rua/Avenida')),
                ('numero_rua_av', models.CharField(max_length=10, verbose_name='Número')),
                ('bairro', models.CharField(max_length=100, verbose_name='Bairro')),
                ('pais', models.CharField(max_length=50, verbose_name='País')),
                ('uf', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=2, verbose_name='UF')),
                ('cidade_municipio', models.CharField(max_length=100, verbose_name='Cidade/Município')),
                ('complemento', models.CharField(blank=True, max_length=255, null=True, verbose_name='Complemento')),
                ('telefone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefone')),
                ('telefone2', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefone 2')),
                ('celular', models.CharField(blank=True, max_length=15, null=True, verbose_name='Celular')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('fax', models.CharField(blank=True, max_length=15, null=True, verbose_name='Fax')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20, unique=True, verbose_name='Código')),
                ('tipo_pessoa', models.CharField(choices=[('F', 'Física'), ('J', 'Jurídica')], max_length=1, verbose_name='Tipo de Pessoa')),
                ('cpf_cnpj', models.CharField(max_length=18, unique=True, verbose_name='CPF/CNPJ')),
                ('rg_ie', models.CharField(blank=True, max_length=15, null=True, verbose_name='RG/IE')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], max_length=1, verbose_name='Sexo')),
                ('carteira_trabalho', models.CharField(blank=True, max_length=20, null=True, verbose_name='Carteira de Trabalho')),
                ('data_nascimento', models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')),
                ('insc_municipal', models.CharField(blank=True, max_length=20, null=True, verbose_name='Inscrição Municipal')),
                ('razao_social', models.CharField(blank=True, max_length=100, null=True, verbose_name='Razão Social')),
                ('cep', models.CharField(max_length=10, verbose_name='CEP')),
                ('rua_av', models.CharField(max_length=255, verbose_name='Rua/Avenida')),
                ('numero_rua_av', models.CharField(max_length=10, verbose_name='Número')),
                ('bairro', models.CharField(max_length=100, verbose_name='Bairro')),
                ('pais', models.CharField(max_length=50, verbose_name='País')),
                ('uf', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=2, verbose_name='UF')),
                ('cidade_municipio', models.CharField(max_length=100, verbose_name='Cidade/Município')),
                ('complemento', models.CharField(blank=True, max_length=255, null=True, verbose_name='Complemento')),
                ('telefone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefone')),
                ('telefone2', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefone 2')),
                ('celular', models.CharField(blank=True, max_length=15, null=True, verbose_name='Celular')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('fax', models.CharField(blank=True, max_length=15, null=True, verbose_name='Fax')),
            ],
            options={
                'verbose_name': 'Fornecedor',
                'verbose_name_plural': 'Fornecedores',
            },
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20, unique=True, verbose_name='Código')),
            ],
            options={
                'verbose_name': 'Funcionário',
                'verbose_name_plural': 'Funcionários',
            },
        ),
        migrations.CreateModel(
            name='OutroModulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20, unique=True, verbose_name='Código')),
            ],
            options={
                'verbose_name': 'Outro Módulo...',
                'verbose_name_plural': 'Outros Módulos...',
            },
        ),
    ]
