from product import Product

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self):
        product_name = input("White the product name: ")
        product_price = int(input("White the product price: "))
        self.items.append(Product(product_name, product_price))
        print(f"\n{product_name.title()} added to cart.")

    def show_cart(self):
        if self.items:
            print("Cart items:")
            for item in self.items:
                print(f"- {item.name.title()} (${item.price})")
        else:
            print("Cart is empty!")

    def get_total(self):
        total = 0
        for item in self.items:
            total += item.price

        print(f"Total: ${total}")
        print("Thank you for shopping!")