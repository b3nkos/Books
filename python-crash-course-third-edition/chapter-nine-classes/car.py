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


my_car = Car("Toyota","Corolla", 2020)
my_car.update_odometer(100)
my_car.increment_odometer(50)
my_car.read_odometer()
