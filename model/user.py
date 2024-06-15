class User:
    def __init__(self, username, user_type):
        self.username = username
        self.user_type = user_type

    def __repr__(self):
        return f'User(username={self.username}, user_type={self.user_type})'

    def get_user_info(self):
        return f'Username: {self.username}, User Type: {self.user_type}'