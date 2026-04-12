response = ""
users = {}

while response != "no":
    vacation = input("Where do you want to go on vacation?\n")
    user_name = input("What is your name?\n")
    response = input("Whould you like to continue? yes/no\n")
    users[user_name] = vacation

print("")
for user_name, vacation in users.items():
    print(f"{user_name.title()} would like to visit {vacation.title()}.")

