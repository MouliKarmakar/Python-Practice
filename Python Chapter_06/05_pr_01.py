a = input("enter the 1st digit here :\n")
b = input("enter the 2nd digit here :\n")
c = input("enter the 3rd digit here :\n")
d = input("enter the 4th digit here :\n")

a= int(a)
b = int(b)
c = int(c)
d = int(d)

if(a>d):
    f1 = a
else:
    f1 =d

if(b>c):
    f2 = b
else:
    f2 =c

if(f1>f2):
    print("f1 is greatest")
else:
    print("f2 is greatest") 
print(f1)                       

