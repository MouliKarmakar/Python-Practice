for i in range(1,6):
    for j in range(1,6-i):
        print(" ",end="")
    for k in range(1,(2*i)):
        print("*",end="")
    print("\n")

for l in range(4,0,-1):
    for m in range(-1,4-l):
        print(" ",end="")
    for n in range((2*l-1),0,-1):
        print("*",end="")
    print("\n")

