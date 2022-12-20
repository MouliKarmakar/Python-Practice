letter = '''Dear <|NAME|>
i am so glad to inform you that you have been selected by the 
ABC progming house. 
        wish you good luck for your new starting job
date : <|DATE|>'''
name = input( "enter your name :")
date = input("enter date :")
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
print(letter)