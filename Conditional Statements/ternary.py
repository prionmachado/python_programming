#this is single line if/ ternary operator

#example 1
food = input("food :")
eat = "yes" if food == "cake" else "no"
print(eat)

#example 2
food = input("food : ")
print("Sweet") if food == "cake" or food == "jalebi" else print("not sweet") 

#this is clever if/ ternary operator 

#example 1
age = int(input("age : "))
vote = ("yes", "no") [age<18] 
print(vote) 

#example 2
sal = float(input("Salary: "))
tax = sal*(0.1, 0.2) [sal<=50000]
print(tax) 
