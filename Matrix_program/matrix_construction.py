row = int(input("enter how many row you want : "))
coloum = int(input("enter how many coloum you want : "))
print("enter the digits for matrix here :")
matrix = [[int(input())for i in range(row)]for j in range(coloum) ]
print()
print("the materix is : ")
for i in range(row):
    for j in range(coloum):
        print(format(matrix[i][j],"<3"),end="")
    print("\n")
