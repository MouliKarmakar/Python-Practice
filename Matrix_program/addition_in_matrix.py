row = int(input("enter how many row you want : "))
coloum = int(input("enter how many coloum you want : "))

print("enter the digits for matrix here :")
matrix1 = [[int(input())for i in range(row)]for j in range(coloum) ]
print()

print("the materix1 is : ")
for i in range(row):
    for j in range(coloum):
        print(format(matrix1[i][j],"<3"),end="")
    print("\n")

print("enter the digits for matrix here :")
matrix2 = [[int(input())for i in range(row)]for j in range(coloum) ]
print()

print("the materix2 is : ")
for i in range(row):
    for j in range(coloum):
        print(format(matrix2[i][j],"<3"),end="")
    print("\n")

result = [[0 for i in range (row)] for j in range(coloum)]

for i in range(row):
    for j in range(coloum):
        result[i][j] =(matrix1[i][j]+matrix2[i][j])

print("the result is :")
for i in range(row):
    for j in range(coloum):        
        print(format(result[i][j],"<3"),end="") 
    print("\n")           

