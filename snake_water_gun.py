import random

def gameWin(comp,you):
    if comp == you :
        return None
    
    elif comp == 'S':
        if you == 'w':
            return False
        elif you == 'G':
            return True
    
    elif comp == 'W':
        if you == 'G':
            return False
        elif you == 'S':
            return True 
    
    elif comp == 'G':
        if you == 'S':
            return False
        elif you == 'W':
            return True    
                    
print("computer's turn: Snake(S) Water(W) or Gun(G) ?")
randomNo = random.randint(1,3)
if randomNo ==1:
    comp ='S'
elif randomNo == 2:
    comp = 'W'
else:
    comp = 'G'        

you = input("your turn: Snake(S) Water(W) or Gun(G) ?")
a = gameWin(comp,you)

print(f"Computer chose :{comp}")
print(f"You choose :{you}")

if a == None:
    print("The game is a tie.")
elif a == False:
    print("You lose.")
else:
    print(" Congratulations ,you win.")    

