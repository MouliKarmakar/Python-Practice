def gamescore():
    return 67854

score = gamescore()
with open("Hiscore.txt") as f:
    hiscore = int(f.read())

if score>int(hiscore) :
    with open("Hiscore.txt","w") as f:
        f.write(str(score))    
    

