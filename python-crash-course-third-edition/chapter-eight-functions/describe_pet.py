def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type}.\nMy {animal_type}'s name is {pet_name.title()}\n")

describe_pet("dog", "rex")
describe_pet(pet_name="whiskers", animal_type="cat")