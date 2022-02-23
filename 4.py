from turtle import pen


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def abautME(self):
        print(f"name: {self.name} salary: {self.age}")



class Employee(Person):
    def __init__(self, name, age, salary): 
        self.name = name
        self.age = age
        self.salary = salary
    
    def salaryEmployee(self):
        print(f"{self.name}'s salary is {self.salary} and age of{ self.age}")

person = Person(input("type your name: "), input("type your age: "))
person.abautME()
employee = Employee(input("type your name: "), input("type your age: "), int(input("type your salary: ")))
employee.salaryEmployee()
