class House:
    def __init__(self, owner, location, bedrooms, price):
        self.owner = owner
        self.location = location
        self.bedrooms = bedrooms
        self.price = price

    def display_info(self):
        return (
            f"This house belongs to {self.owner}, "
            f"is located in {self.location}, "
            f"has {self.bedrooms} bedrooms "
            f"and costs ${self.price}."
        )

    def update_price(self, new_price):
        self.price = new_price

    def add_bedroom(self):
        self.bedrooms += 1


# creating house object instances
house1 = House("Ian Koech", "Nairobi", 3, 7500000)
house2 = House("Alice", "Mombasa", 4, 9500000)

print(house1.display_info())
print(house2.display_info())

# updating object data
house1.update_price(8000000)
house1.add_bedroom()

print(house1.display_info())
