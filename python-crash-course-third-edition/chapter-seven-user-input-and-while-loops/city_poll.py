cities = []

while True:
    response = input("Which city would you like to visit? or type quit to exit\n")
    if response == "quit":
        break
    cities.append(response)

for city in cities:
    print(f"I'd love to go to {city.title()}!")