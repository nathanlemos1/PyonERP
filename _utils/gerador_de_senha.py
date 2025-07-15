import bcrypt
# Solicita o usuário
user = input("Digite a o usuário: ")

# Solicita a senha do usuário
password = input("Digite a senha para o usuário: ")

papel = input("Digite o numero do papel: ")

# Gera o hash da senha com bcrypt
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Converte o hash para uma string no formato adequado para SQL
hashed_password_str = hashed_password.decode('utf-8')

# Monta o comando SQL
sql = f"""
INSERT INTO usuarios (nome, email, senha, papel) 
VALUES ('{user}', '{user}@pyonerp.com', '{hashed_password_str}', {papel});
"""

# Imprime o comando SQL
print("\nComando SQL gerado:")
print(sql)