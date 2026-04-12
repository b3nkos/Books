class Restaurant:
    def __init__(self, name, cuisine_type, number_served=0):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"{self.name.title()} serves {self.cuisine_type.title()} cuisine.")
        print(f"Number served: {self.number_served}")

    def open_restaurant(self):
        print(f"{self.name.title()} is open.")

    def set_number_served(self, number_served):
        self.number_served = number_served


restaurant = Restaurant("Pizza Place", "italian")
restaurant.open_restaurant()
restaurant.set_number_served(25)
restaurant.describe_restaurant()
