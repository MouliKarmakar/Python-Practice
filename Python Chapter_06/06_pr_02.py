num1 =input("enter marks 1 :\n")
num2 =input("enter marks 2 :\n")
num3 =input("enter marks 3 :\n")
num1 =int(num1)
num2 =int(num2)
num3 =int(num3)

if(num1<33 or num2<33 or num3<33):
    print("you are fail due to less than 33 marks in perticuler sub")
if((num1+num2+num3)/3<40): 
    print("you are fail due to less than 40 marks in total")  
else:
    print("you are pass")    