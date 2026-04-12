favorite_numbers = {
    "jose": 7,
    "maria": 3,
    "luis": 10
}

favorite_numbers["maria"] = 5
favorite_numbers["andres"] = 8

for key, value in favorite_numbers.items():
    print(f"{key.capitalize()}'s favorite number is {value}")