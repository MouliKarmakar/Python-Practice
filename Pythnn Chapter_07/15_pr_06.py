# n! = 1 x 2 x 3 x 4 x.......n!
# 5! = 1 x 2 x 3 x 4 x 5 
num = input("enter the number here :\n")
num = int(num)
factiorial =1
for i in range (1,num+1):
    factiorial = factiorial*i
print(f"the factoral of {num} is {factiorial}")    