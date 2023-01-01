for i in range(1,5):
    for j in range(1,i+1):
        print("* ",end="")
    for k in range(0,(8-(2*i))):
        print("  ",end="")
    for l in range(1,i+1):
        print("* ",end="")
    print("\n")

