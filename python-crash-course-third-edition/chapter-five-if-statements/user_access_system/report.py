def show_report(users, attemps):
    for i in range(4):
        if attemps[i] == 0:
            print(f"{users[i]}: Account locked")
        else:
            print(f"{users[i]}: {attemps[i]} attemps remaining")