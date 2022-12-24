class Employee:
    company ="Google"

    def Get_Salary(self):
        print("your salary is 100k")
    @staticmethod
    def greet ():
        print("good morning sir.")

harry = Employee()
harry.salary =1000000
harry.greet()
harry.Get_Salary()        