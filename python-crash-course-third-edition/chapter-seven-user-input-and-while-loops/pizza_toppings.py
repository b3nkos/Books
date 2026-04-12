toppings = []

response = ""

while response != "quit":
    topping = input("Which topping whould you like to add?\n")
    toppings.append(topping)
    response = input("Would you like to add another topping? or write quit to exit\n")

for topping in toppings:
    print(f"Added {topping} to your pizza.")