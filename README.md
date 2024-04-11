![sistema](https://raw.githubusercontent.com/LSouza3PS/Django/develop/static/app/img/sistema.png)

# Projeto Fictício: Sistema de Gestão de Serviços com Django

Este é um projeto bastante simplificado e fictício, somente com o intuito de demonstrar minhas habilidades em desenvolvimento web usando o framework Django e Tailwindcss.

O Sistema de Gestão de Serviços oferece uma plataforma exemplificando a organização dos serviços, mostrando todo conceito de CRUD e sistemas MVC / MTV.

## Funcionalidades Principais:

- **Criar / Editar / Visualizar / Filtrar / Excluir:** Serviços, Clientes, Solicitações, Usuários e Grupo de Usuários de maneira fácil e rápida;
- **Segurança:** Pode gerir usuários dando devidos acessos com a criação de grupos;
- **Responsividade:** Acessar o sistema em Celulares, Tablets e Notebooks.

## Tecnologias Utilizadas:

- **Django:** Framework web Python para desenvolvimento rápido e eficiente.
- **Tailwindcss:** Desenvolvimento de interfaces responsivas e dinâmicas.
- **Banco de Dados SQLite:** Armazenamento eficiente e fácil configuração para projetos menores.

## Como Executar o Projeto:

1. Clone este repositório: `git clone https://github.com/LSouza3PS/Django.git`
2. Crie e ative um ambiente virtual: `python -m venv env` e `source env/bin/activate` (ou `env\Scripts\activate` no Windows).
3. Instale as dependências: `pip install -r requirements.txt`
4. Aplique as migrações: `python manage.py migrate`
5. Crie um usuário: `python manage.py createsuperuser` (configure o nome de usuário, e-mail e senha).
6. Inicie o servidor de desenvolvimento: `python manage.py runserver`

Acesse [http://localhost:8000/](http://localhost:8000/) em seu navegador para explorar o Sistema de Gestão de Serviços.

Fique à vontade para contribuir, reportar problemas ou sugerir melhorias. Este projeto é uma demonstração das minhas habilidades em Django, e estou aberto a feedbacks construtivos.
