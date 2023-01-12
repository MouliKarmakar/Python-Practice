row = int(input("how many row you want ?\n"))
column = int(input("how many column you want ?\n"))

print("enter the digits for matrix1.")
matrix1 =[[int(input())for i in range(row)]for j in range(column)]

print("matrix1 is :")
for i in range(row):
    for j in range(column):
        print(format(matrix1[i][j],"<3"),end="")
    print("\n")

print("enter the digits for matrix2.")
matrix2 =[[int(input())for i in range(row)]for j in range(column)]

print("matrix2 is :")
for i in range(row):
    for j in range(column):
        print(format(matrix2[i][j],"<3"),end="")
    print("\n")

result =[[0 for i in range(row)]for j in range(column)]

for i in range(row):
    for j in range(column):
        result[i][j] =(matrix1[i][j]-matrix2[i][j])

print("the result is:")
for i in range(row):
    for j in range(column):
        print(format(result[i][j],"<3"),end="")
    print("\n")

        