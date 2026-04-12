def make_pizza(*toppings):
    print("Making a pizaa with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza("cheese", "pepperoni", "olives")