num1 = input("enter the first number here :\n")
num2 = input("enter the second number here :\n")
num3 = input("enter the third number here :\n")
num4 = input("enter the fourth number here :\n")

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
num4 = int(num4)

if (num1>num2):
    f1 = num1
else:
    f1 = num2

if(num3>num4):
    f2 = num3
else:
    f2 = num4

if(f1>f2):
    print("the greatest number is :",f1)
else:
    print("the greatest number is :",f2)  
          


