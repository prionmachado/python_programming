#---------------------Chapter 4 : Dictionaries vand Sets----------------------

#-----Dictionary in python -----
#A dictionary is a collection of key-value pairs and an mutable datatype

#syntax ---->
#dict = {'key1':'value1','key2':'value2'}
info = {
    'name':'Johan',
    'age':25,
} 
print(info['name'])
print(info['age']) 

#we can use nested dictionary also

#---Dictionary methods---
# 1. dict.keys() : returns all keys
# 2. dict.values() : returns all values
# 3. dict.items() : returns all key-value pairs
# 4. dict.get(key) : returns the value for the given key
# 5. dict.update() : updates the dictionary with the items
# 6. dict.pop(key) : removes the item with the specified key and returns the value
# 7. dict.clear() : removes all elements from the dictionary
# 8. dict.copy() : returns a copy of the dictionary

print(info.keys())
print(info.values())
print(info.items()) 
print(info.get("name"))
print(info.pop("name"))
print(info.copy())
info.update({"name" : "Prion"})
print(info) 

print(info.clear()) 

#-----Sets in python-----

number = {1,2,3,4}
print(number)
number1 = {1,3,2,2,2}   #Repeated elements are stored once
print(number1)

#Empty set syntax ----->
null_set = set()
print(null_set)

#Sets are mutable we can add or remove an element but the elements are immutable we can't change the value of element.

#---Set methods--- 
# 1. set.add(element) : adds an element to the set
# 2. set.remove(element) : removes the element from the set
# 3. set.clear() : Empties the set
# 4. set.pop() : pops(removes) a random value
# 5. set.union(set2) : combines both set values and returns a new set
# 6. set.intersection(set2) : combines common values and returns new set

number.add(5)
print(number)

number.remove(1)
print(number)

number.pop()
print(number)

print(number.union(number1))
print(number.intersection(number1))

number.clear()
print(number) 
