from core.auth import Auth
from core.session import SessaoAtual
from view.login_view import LoginView

class AuthController:
    def __init__(self, root):
        self.auth = Auth()
        self.session = SessaoAtual()
        self.login_view = LoginView(root, self)

    def attempt_login(self, email, password):
        user = self.auth.login(email, password)
        if user:
            self.session.login(user['id'], user['nome'], user['papel'])
            return True
        return False

    def logout(self):
        self.session.logout()
        self.login_view.show()