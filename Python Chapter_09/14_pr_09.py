with open("this.txt")as f1:
    file1 = f1.read()

with open("copy.txt") as f2:
    file2 = f2.read()

if (file1 ==file2) :
    print("these files are identical.")
else:
    print("these files are not identical.")    
