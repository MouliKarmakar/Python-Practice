class Employee:
    company ="Google"

    def __init__(self,name,salary):
        self.name = name
        self.salary= salary
        print("company haired you .")

    def get_details(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of this employee is {self.salary}")


    def Get_Salary(self):
        print("your salary is 100k")
    @staticmethod
    def greet ():
        print("good morning sir.")

harry = Employee("harry",190)
harry.get_details()
