collection = set()
collection.add(1)   #adds element
collection.add(2)
collection.add(2)  #python will ignore this element
collection.add("prion")
collection.add((1,2,3))
#collection.add([1,2,3])  #never add list it will give error

collection.remove(1)   #removes element
print(collection) 

collection1 = set()

collection1.add(1)
collection1.add(2)

collection1.clear()   #clears the set
print(collection1)
print(len(collection1))

collection2 = {"hello","world","python"}
print(collection2.pop())  # pops any random element from the set 
print(collection2.pop())
print(collection2.pop()) 

set1 = {1,2,3}
set2 = {2,3,4}
print(set1.union(set2))   #combines both set values and returns new set
print(set1.intersection(set2))  #combines common values and returns it 