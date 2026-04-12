favorite_places = {
    "Jose": ["Tokyo", "Berlin"],
    "Maria": ["Paris"],
    "Luis": ["New York", "Toronto", "Sydney"]
}

for person, places in favorite_places.items():
    print(f"{person}'s favorite places:")
    for place in places:
        print(f"- {place}")
    print()