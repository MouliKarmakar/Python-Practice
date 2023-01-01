for i in range(1,5):
    for k in range(1,5-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print("\n")

for l in range(4,0,-1):
    for m in range(0,4-l):
        print(" ",end="")
    for n in range(l,0,-1):
        print("*",end="")
    print("\n")
