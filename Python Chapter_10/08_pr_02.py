class Calculator:
    def __init__(self,num):
        self.number = num
        # self.square = square
        # self.square_root = square_root
    def square(self):
        print(f"the value of square of {self.number} is {self.number**2}")
    def square_root(self):
        print(f"the value of square_root of {self.number} is {self.number**(1/2)}")
    def cube(self):
        print(f"the value of cube of {self.number} is {self.number**3}")

   
a = Calculator(4)
a.square()
a.square_root()
a.cube()



