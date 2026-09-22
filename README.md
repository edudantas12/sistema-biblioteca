# Sistema de Biblioteca

Sistema de gerenciamento de biblioteca desenvolvido em Python, com PostgreSQL como banco de dados.

## Funcionalidades

- Cadastro de livros
- Listagem de livros
- Busca de livros por ID
- Atualização de livros
- Exclusão de livros
- Cadastro de usuários
- Listagem de usuários
- Busca de usuários por ID
- Atualização de usuários
- Exclusão de usuários
- Realização de empréstimos
- Devolução de livros

## Tecnologias utilizadas

- Python
- PostgreSQL
- Psycopg
- python-dotenv
- PyCharm

## Estrutura do projeto

```text
sistema_biblioteca/
├── banco.py
├── emprestimos.py
├── livros.py
├── main.py
├── usuarios.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Instalação

Clone o repositório:

```bash
git clone https://github.com/edudantas12/sistema-biblioteca.git
```

Entre na pasta:

```bash
cd sistema_biblioteca
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Configuração

Crie um arquivo `.env` na raiz do projeto com as configurações do banco de dados:

```env
DB_USER=postgres
DB_NAME=biblioteca
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432
```

## Execução

Execute o arquivo principal:

```bash
python main.py
```
