letter = '''Dear <|NAME|>
I am happy to inform you that your have been selected
by the ABC programing house 
Date :<|DATE|>'''
name = input("enter your name :\n")
date = input("enter date :")
letter =letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
print(letter)