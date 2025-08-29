# nested dictionary

student = {
    "name": "Prion",
    "age": 18,
    "subjects" : {
        "math": 90,
        "science": 85,
        "english": 88
    }
} 

print(student["subjects"])

# accessing nested dictionary
print(student["subjects"]["math"]) 

