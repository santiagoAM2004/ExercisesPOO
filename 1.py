class Employee():

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def tax(self):
        if self.salary > 3000:
            print(f"{self.name} have to pay the tax, {self.salary}")
        else:
            print(f"{self.name}'s salary isn't big enough, {self.salary}")

employee = Employee(input("type your name: "), int(input("type your salary: ")))
employee.tax()