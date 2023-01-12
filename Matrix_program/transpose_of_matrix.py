p = int(input("enter the number of row :"))
q = int(input("enter the number of column :"))

print("enter the digits for matrix :")
matrix =[[int(input()) for i in range(q)]for j in range(p)]

print("the matrix is :")
for i in range(p):
    for j in range(q):
        print(format(matrix[i][j],"<3"),end="")
    print("\n")

result = [[0 for i in range(p)]for j in range(q)]

for i in range(q):
    for j in range(p):
        result[i][j] = matrix[j][i]

print("the result is :")
for i in range(q):
    for j in range(p):
        print(format(result[i][j],"<3"),end="")
    print("\n")   
     
