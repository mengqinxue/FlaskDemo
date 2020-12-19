class User:
    def __init__(self, username, password, phone=None):
        self.username = username
        self.password = password
        self.phone = phone

    def user_update(self, phone):
        self.phone = phone

