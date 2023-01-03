for i in range(0,4):
    for j in range(0,4-i-1):
        print("  ",end="")
    for k in range(0,i+1):
        print("*   ",end="")
    for l in range(0,4-i-1):
        print("    ",end="")
    for m in range(0,i+1):
        print("*   ",end="")     
    print("\n")   

for n in range(6,0,-1):
    for o in range(1,6-n):
        print("    ",end="")
    for p in range(1,2*n-3):
        print("*    ",end="")
    print("\n")    

