words = ["kaddu","donkey","mote"]

with open("donkey.txt") as f:
    content = f.read()

for word in words:
    content = content.replace(word,"$%^$#") 
with open("donkey.txt","w") as f:
    content= f.write(content)   