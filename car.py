class Car:
    def __init__(self, brand, model, color, mileage):
        self.brand = brand
        self.model = model
        self.color = color
        self.mileage = mileage

    def update_mileage(self, new_mileage):
        self.mileage = new_mileage

    def display_info(self):
        return (
            f"My car's brand is {self.brand} and model is {self.model}. "
            f"It is {self.color} and has a mileage of {self.mileage} km."
        )


my_car = Car("Toyota", "Corolla", "Black", 34000)
my_car2 = Car("Mazda", "Atenza", "Dark Gray", 23000)

print(my_car.display_info())

my_car.update_mileage(45000)
print(my_car.display_info())
