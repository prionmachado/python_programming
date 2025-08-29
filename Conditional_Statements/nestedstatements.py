name = input("Enter your name:")
b = int(input("Are you citizen of india(press 1 for yes and 0 for no):"))
if b == 1:
    age = int(input("Enter your age:"))
    if age>=18:
        print(name,",you are eligible to vote")
    else:
        print(name,",you are not eligible to vote")
elif b == 0:
    print(name,",you are not eligible to vote")
else:
    print("Invalid input") 


age = int(input("Enter your age:"))
if age>=18:
    if age>=80:
        print("Cannot drive")
    else:
        print("Can drive")
else:
    print("Cannot drive") 
