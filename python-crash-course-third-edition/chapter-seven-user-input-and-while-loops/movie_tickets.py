active = True
response = ""

while active:
    response = input("How old are you? or type quit to stop\n")
    if response == "quit":
        active = False
    elif int(response) >= 40:
        print("Tiket price: $15")
    elif int(response) >= 15:
        print("Tiket price: $10")
    else:
        print("Ticket price: Free")