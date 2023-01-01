for l in range(5,0,-1):
    for m in range(0,5-l):
        print(" ",end="")
    for n in range((2*l-1),0,-1):
        print("*",end="")
    print("\n")    

for i in range(1,6):
    for k in range(1,6-i):
        print(" ",end="")
    for j in range(1,(2*i)):
        print("*",end="")
    print("\n")  