# Manual do Usuário - PyOnERP

## Introdução
O PyOnERP é um sistema ERP simples e modular, projetado para pequenas empresas gerenciarem usuários e permissões. Esta versão inicial foca no login e autenticação.

## Tela de Splash
Ao iniciar o PyOnERP:
1. Uma tela de boas-vindas exibe "Bem-vindo ao PyOnERP".
2. Uma barra de progresso é preenchida gradualmente.
3. Após a conclusão, a tela de login é exibida.

## Tela de Login
1. Insira seu **email** e **senha** nos campos fornecidos.
2. Clique em "Login".
3. Se as credenciais estiverem corretas, uma mensagem de sucesso aparece.
4. Caso contrário, uma mensagem de erro é exibida.

## Observações
- Para o primeiro acesso, um administrador deve criar um usuário no banco de dados (tabela `usuarios`).
- Logs de atividades são salvos em `pyonerp.log`.