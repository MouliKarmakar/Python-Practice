import random

def gamewin(comp,you):
    if comp == you:
        return None

    elif comp == "R":
        if you =="S":
            return False
        elif you =="P":
            return True   

    elif comp == "P":
        if you =="R":
            return False
        elif you =="S":
            return True   

    elif comp == "S":
        if you =="P":
            return False
        elif you =="R":
            return True                    

print ("computer chose : rock(R) paper(p) or scissors(S) ?")
randomno = random.randint(1,3)
if randomno == 1:
    comp = "R"
elif randomno == 2:
    comp = "P"
else:
    comp = "S"

you = input("you choose : rock(R) paper(p) or scissors(S) ?")

a = gamewin(comp,you)
print(f"computer chose {comp}")
print(f"you choose {you}")

if a == None:
    print("this game is a tie.")
elif a == False:
    print("You lose.")
else:
    print("Congratulation,you win the game.")    




