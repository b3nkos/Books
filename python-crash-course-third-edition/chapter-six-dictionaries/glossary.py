glossary = {
    "list": "A collection of items in a particular order",
    "dictionary": "A collection of key-value pairs",
    "tuple": "An immutable list"
}

for key, value in glossary.items():
    print(f"{key.title()}:\n\t{value.title()}\n")