with open("this.txt","r") as f:
    content = f.read()
with open("copy.txt","w") as f :
    copy = f.write(content)    