p = int(input("enter row number you want for matrix1 :"))
n = int(input("enter column for matrix1/row for matrix2 :"))
q = int(input("enter column number for matrix2 :"))

print("enter the digits for matrix1 :")
matrix1 =[[int(input()) for i in range(p)]for j in range(n)]

print("matrix1 is :")
for i in range(p):
    for j in range(n):
        print(format(matrix1[i][j],"<3"),end="")
    print("\n")

print("enter the digits for matrix2 :")
matrix2 =[[int(input()) for i in range(n)]for j in range(q)]

print("matrix2 is :")
for i in range(n):
    for j in range(q):
        print(format(matrix2[i][j],"<3"),end="")
    print("\n")    

result = [[0 for i in range(p)]for j in range(q)]
for i in range(p):
    for j in range(q):
        for k in range(n):
            result[i][j] =result[i][j]+(matrix1[i][k] * matrix2[k][j])

print("now the result is :")
for i in range(p):
    for j in range(q):
        print(format(result[i][j],"<3"),end="")
    print("\n")

