unconfirmed_users = ["alice", "bob", "charlie"]
confirmed_users = []

while unconfirmed_users:
    user = unconfirmed_users.pop()
    print(f"Confirming user: {user}")
    confirmed_users.append(user)

print("\nConfirmed users:")
for user in confirmed_users:
    print(user)