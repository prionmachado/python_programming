import csv 

students = [] 

with open("File/fstudent.csv") as file:
    reader = csv.DictReader(file) 
    for row in reader:
        students.append(row)  #{"Name":row["Name"], "House":row["House"]}

for student in sorted(students, key=lambda student: student["Name"]):
    print(f"{student['Name']} is in {student['House']}")  