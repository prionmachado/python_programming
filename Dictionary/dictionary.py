dict = {
    "key" : "value",
    "name" : "rion",
    "age" : "18",
    "cgpa" : "9.6",
    "subjects" : ["python","c","maths"],
    "language" : ("marathi","hindi","english"),
    "learning" : "coding",
    12 : 45           # we can use int float char boolean or anything in key but not list and dictionaries 
} 

print(dict) 
print(type(dict)) 

print(dict["name"])
print(dict["age"])
print(dict["cgpa"])
print(dict["subjects"])
print(dict["language"])
print(dict["learning"])
print(dict[12]) 

dict["name"] = "Prion"    #new value assigned
dict["surname"] = "Machado"  # new value added
print(dict) 

print(len(dict)) 