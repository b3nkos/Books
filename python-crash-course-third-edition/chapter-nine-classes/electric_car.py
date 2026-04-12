class Car:
    def __init__(self, make, model, year, odometer_reading=0):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = odometer_reading

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, value):
        self.odometer_reading = value

    def increment_odometer(self, value):
        self.odometer_reading += value

class Battery:
    def __init__(self, size):
        self.size = size

    def describe_battery(self):
        print(f"This car has a {self.size}-KWh battery.")


class ElectricCar(Car):
    def __init__(self, make, model, year, odometer_reading=0):
        super().__init__(make, model, year, odometer_reading)
        self.battery = Battery(75)

my_tesla = ElectricCar("Tesla", "Model S", 2023)
my_tesla.battery.describe_battery()