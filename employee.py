
# Define an Employee class
class Employee:
    def __init__(self, name, position, salary):
        self.name = name  # Employee's name (attribute)
        self.position = position  # Employee's job title (attribute)
        self.salary = salary

    def introduce(self):
        return f"Hi, I'm {self.name} and I work as a {self.position}."

    def give_raise(self, amount):
        self.salary += amount

    def get_info(self):
        return f"Employee: {self.name}, Position: {self.position}, Salary: ${self.salary}"


# Creating instances of Employee
employee1 = Employee("Alice", "Software Engineer", 76000)
employee2 = Employee("Bob", "Data Scientist", 66000)

# Accessing attributes
print(employee1.name)
print(employee2.position)

print(employee1.get_info())
print(employee2.get_info())
# Calling the introduce method
print(employee1.introduce())
print(employee2.introduce())
# using instance methods
employee2.give_raise(5000)
print(employee2.get_info())
