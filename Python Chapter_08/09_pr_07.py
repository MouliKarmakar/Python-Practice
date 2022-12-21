def remove_and_strip(string,word):
    newstr = string.replace(word ,"")
    return newstr.strip()

text ="    Noun is a naming word   "
new = remove_and_strip(text,"Noun")
print(new)
