file=open("poem.txt","r")
poem = file.read()
print(poem)

if "twinkle" in poem :
    print("twinkle is in the text.")
else:
    print("twinkle is not in the text.") 
file.close()       