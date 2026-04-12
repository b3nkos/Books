from admin import Admin

admin = Admin("jose", "jose@email.com", ["add", "delete", "ban"])
admin.describe_user()
admin.show_privileges()