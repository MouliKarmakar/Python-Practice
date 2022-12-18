# a = {1,4,3,5,}
a = {1,4,3,5,1}
print(a)
print(type(a))

# important : this syntax will create an empty dictonary not an empty set
b ={}
print(type(b))

# important : this syntax will create an empty set not an empty dictonary
c = set()
print(type(c))

# adding value to an empty set
c.add(3)
c.add(7)
print(c)
# adding a repitative value does not change a set

# c.add([5,6,8]) # we cant add a list or dictionary in a set
# print(c)
c.add((4,5,6)) # we can add a tuple in a set
print(c)

print(len(c)) #prints the length of a set
c.remove(7) # removes 7 from the set
print(c)
c.pop()
print(c)







