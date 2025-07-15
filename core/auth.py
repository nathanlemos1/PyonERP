import bcrypt
import logging
from core.database import Database
from core.session import SessaoAtual

class Auth:
    def __init__(self):
        self.db = Database()

    def hash_password(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, password, hashed):
        # Converte bytearray para bytes, se necessário
        if isinstance(hashed, bytearray):
            hashed = bytes(hashed)
        return bcrypt.checkpw(password.encode('utf-8'), hashed)

    def login(self, email, password):
        query = "SELECT id, nome, senha, papel FROM usuarios WHERE email = %s"
        result = self.db.execute_query(query, (email,), fetch=True)
        if result and len(result) > 0:
            user = result[0]
            if self.check_password(password, user['senha']):
                logging.info(f"Usuário {email} autenticado com sucesso.")
                return user
            else:
                logging.warning(f"Tentativa de login inválida para {email}.")
        return None

    def can(self, permission):
        if not SessaoAtual().is_authenticated():
            return False
        query = """
            SELECT 1 FROM papel_permissao pp
            JOIN permissoes p ON pp.permissao_id = p.id
            WHERE pp.papel_id = %s AND p.nome = %s
        """
        result = self.db.execute_query(query, (SessaoAtual().user_role, permission), fetch=True)
        return len(result) > 0