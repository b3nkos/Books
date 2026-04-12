from cart import Cart

cart = Cart()
active = True

print("🛒 Online Store")

while active:
    print("\n1. Add to cart")
    print("2. View cart")
    print("3. Checkout")

    option = int(input("Choose an option: "))

    if option == 3:
        cart.get_total()
        active = False
    elif option == 1:
        cart.add_item()
    elif option == 2:
        cart.show_cart()