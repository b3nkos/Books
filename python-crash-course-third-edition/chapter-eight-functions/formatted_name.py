def get_formatted_name(first, last):
    return f"{first.title()} {last.title()}"


name = get_formatted_name("jose", "martinez")
print(name)
