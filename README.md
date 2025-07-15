# PyOnERP

PyOnERP é um sistema ERP modular desenvolvido em Python, voltado para iniciantes e intermediários, com interface gráfica em Tkinter e banco de dados MySQL.

## Estrutura do Projeto
- `core/`: Contém configurações, conexão com banco e autenticação.
- `controller/`: Lógica de controle (MVC).
- `view/`: Interfaces gráficas com Tkinter.
- `migrations/`: Scripts SQL para criação do banco.
- `main.py`: Ponto de entrada do sistema.

## Pré-requisitos
- Python 3.x
- Bibliotecas: `mysql-connector-python`, `bcrypt`, `python-dotenv`
- MySQL Server

## Instalação
1. Clone o repositório.
2. Crie um arquivo `.env` com base no `.env-example`.
3. Instale as dependências: `pip install mysql-connector-python bcrypt python-dotenv`.
4. Execute o script de migração `001_create_initial_tables.sql` no MySQL.
5. Rode o sistema: `python main.py`.

## Funcionalidades Atuais
- Tela de splash com barra de progresso.
- Sistema de login com autenticação segura (bcrypt).
- Controle de sessão via singleton `SessaoAtual`.

## Como Usar
1. Ao iniciar, uma tela de splash aparece com uma barra de progresso.
2. Após, a tela de login é exibida. Use um email e senha válidos (cadastre um usuário admin no banco manualmente para o primeiro acesso).
3. O sistema registra logs em `pyonerp.log`.

## Próximos Passos
- Cadastro e listagem de usuários.
- Controle de acesso baseado em permissões (RBAC).