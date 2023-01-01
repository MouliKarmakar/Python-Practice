for i in range(1,5):
    for j in range(1,i+1):
        print("*  ",end="")
    for k in range(0,(8-(2*i))):
        print("   ",end="")
    for l in range(1,i+1):
        print("*  ",end="")
    print("\n")

for m in range(3,0,-1):
    for n in range(1,m+1):
        print("*  ",end="")
    for o in range(0,(8-(2*m))):
        print("   ",end="")
    for p in range(1,m+1): 
        print("*  ",end="")
    print("\n")       

