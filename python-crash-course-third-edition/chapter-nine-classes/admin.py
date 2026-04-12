from user import User

class Admin(User):
    def __init__(self, username, email, privileges):
        super().__init__(username, email)
        self.privileges = privileges

    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")