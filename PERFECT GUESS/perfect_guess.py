import random
randomno = random.randint(1,100)
userguess = None
guess = 0

userguess = input("guess the number:\n")
userguess = int(userguess)
guess += 1
while userguess != randomno:
    userguess = input("guess the number:\n")
    userguess = int(userguess)
    guess += 1
    if userguess == randomno:
        print("you have guessed the right no.")
    else:    
        if userguess > randomno:
            print("your guess is too high.please guess a smeller number.")
        else:
            print("your guess is too small.please guess a bigger number.")

print(f"your number of guess to reach the right number are {guess}")
                 

with open ("highscore.txt","r") as f:
    highscore = f.read()
    if guess < int(highscore) :
        with open ("highscore.txt","w") as f:
            f.write(str(guess))
        print("Congratulation,you break the high-score.")       

                   