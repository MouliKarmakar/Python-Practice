mydict ={
    "fast":"in a quick manner",
    "harry" :"a coder",
    "marks":[ 1,2,3,5],
    "anotherdict":{'Harry':'plyar'},
     4 :2*2 
    }

# Dictionary Methods
# print(type(mydict.keys()))
print(list(mydict.keys())) # print the keys of the dictionary
print(mydict.values()) # print the values of the dictionary
print(mydict.items()) # print the (key,value) for all the contents od dictionary
print (mydict)
updatedict={"lovish":"friend",
"bear":"tolarate",
"beaytiful":"preaty"
}
mydict.update(updatedict) # updates the dictionary by adding key-value paires from updateDict
print(mydict)

print(mydict.get("harry2"))
print(mydict["harry2"])





