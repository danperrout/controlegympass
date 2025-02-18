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