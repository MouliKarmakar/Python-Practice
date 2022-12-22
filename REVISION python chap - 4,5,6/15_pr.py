text = input("enter your text here :\n")

if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
elif("click here" in text):
    spam = True 
else:
    spam = False

if spam:
    print("The text is a spam")
else:
    print("The text is not a spam")  

text.remove(spam)
print(text)                