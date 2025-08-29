student = {
    "name": "Prion",
    "age": 18,
    "subjects" : {
        "math": 90,
        "science": 85,
        "english": 88
    }
} 

print(student.keys())
print(student.values())
print(student.items()) 
print(student.keys())

student.update({"city" : "delhi"})
print(student) 

print(student["name"])
print(student.get("name"))
#print(student["name1"])    #error
#print(student.get("name2"))   #None


