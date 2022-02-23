class Employee2():
    def __init__(self, name, salary = 1000):
        self.name = name
        self.salary = salary

    def printInformations(self):
        print(f"name: {self.name} salary: {self.salary}")

employee2 = Employee2("Mosquera", 3000)
employee2_1 = Employee2("Arias") 
employee2.printInformations()
employee2_1.printInformations()

