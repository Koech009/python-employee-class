# Defining a class called Car
class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color


# creating and instance (an object)of the car class
my_car = Car("Toyota", "Corolla", "Black")
my_car2 = Car("Mazda", "Atenza", "dark-gray")
# accessing attributes
print(my_car.brand)
print(my_car2.brand)
print(my_car.color)
print(my_car2.model)
