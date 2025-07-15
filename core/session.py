class SessaoAtual:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SessaoAtual, cls).__new__(cls)
            cls._instance.user_id = None
            cls._instance.user_name = None
            cls._instance.user_role = None
        return cls._instance

    def login(self, user_id, user_name, user_role):
        self.user_id = user_id
        self.user_name = user_name
        self.user_role = user_role

    def logout(self):
        self.user_id = None
        self.user_name = None
        self.user_role = None

    def is_authenticated(self):
        return self.user_id is not None