with open("sample.txt","r") as f:
    a= f.read()
print(a)

with open("this.txt","w") as s:
    e = s.write("quickly, go and bring the fish bowl here.")
print(e)    