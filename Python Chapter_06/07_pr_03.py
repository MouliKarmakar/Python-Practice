text = input("type your text here :\n")
if("make a lot of money" in text):
    spam =True
elif("bye now" in text):
    spam = True
elif("click this" in text):
    spam = True    
elif("subscribe this" in text):
    spam = True    
elif("in term" in text):
    spam = True 
else:
    spam =False

if(spam):
    print("This text is spam")
else:
    print("This text is not spam")    
               