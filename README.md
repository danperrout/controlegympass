# Controle de Pagamento de Aulas no Gympass (Wellhub)

Este é um projeto Django desenvolvido para ajudar proprietários de academias a controlar o pagamento de aulas no Gympass (Wellhub). Como o Gympass paga apenas 9 aulas por mês, mesmo que o proprietário dê mais aulas, este aplicativo permite o controle de quem já pagou e quantas vezes.

## Funcionalidades

- **Cadastro de Alunos**: Cadastre os alunos que frequentam as aulas.
- **Registro de Aulas**: Registre as aulas dadas por cada aluno.
- **Controle de Pagamento**: Acompanhe quantas aulas já foram pagas pelo Gympass e quantas ainda faltam.
- **Relatórios Mensais**: Gere relatórios mensais para visualizar o total de aulas dadas e o valor devido.

---

## Requisitos

- Python 3.12+
- Django 5+
- Banco de dados SQLite (ou outro de sua preferência)

---

## Passos para Configuração e Execução do Projeto

### 1. Clone o Repositório

Primeiro, clone o repositório para o seu ambiente local:

```bash
git clone https://github.com/danperrout/controlegympass.git
cd controlegympass
```

2. Crie um Ambiente Virtual
Crie um ambiente virtual para isolar as dependências do projeto:

```bash
python -m venv venv
```
No Linux/MacOS:

```bash
source venv/bin/activate
```
No Windows:

```bash
venv\Scripts\activate
```
3. Instale as Dependências
Instale as dependências listadas no arquivo requirements.txt:

```bash
pip install -r requirements.txt
```
4. Configure o Banco de Dados
O projeto usa SQLite por padrão. Para criar as tabelas no banco de dados, execute as migrações:

```bash
python manage.py migrate
```
5. Crie um Superusuário
Crie um superusuário para acessar o painel administrativo do Django:

```bash
python manage.py createsuperuser
```
Siga as instruções para definir um nome de usuário, email e senha.

6. Execute o Servidor de Desenvolvimento
Inicie o servidor de desenvolvimento do Django:

```bash
python manage.py runserver
```
O servidor estará disponível em:
http://127.0.0.1:8000/

7. Acesse o Painel Administrativo
Acesse o painel administrativo do Django para gerenciar alunos, aulas e pagamentos:
http://127.0.0.1:8000/admin/

Use as credenciais do superusuário criado no passo 5.