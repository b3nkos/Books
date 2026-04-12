class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def describe_user(self):
        print(f"User: {self.username}, Email: {self.email}")