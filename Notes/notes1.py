#---------------Chapter 2 : Strings and conditional Statements---------------

#Strings are immutable in python
#---Concatenation of string---
a = "Hello"
b = "World"
c = a+b
print(c)

#---Length of string---
#syntax ----> len(str)
Name = "Prion"
print(len(Name)) 

#---Indexing---
#syntax ----> str[index]
#Note: Indexing starts from 0
Name = "Prion"
print(Name[0])      # P  R  I  O  N   # P   R   I   O   N
#it will print 'P'. # 0  1  2  3  4   #-5  -4  -3  -2  -1    #negative index

#---String slicing---
#syntax ----> str[start:stop:step]
#Note: start is inclusive, stop is exclusive, step is optional
Name = "Prion"
print(Name[0:3])    # it will print 'Pri'
print(Name[0:3:2])  # it will print 'Pi'
print(Name[-3:-1])  # it will print 'io'

#---String functions---
#syntax ----> str.function()
#Note: str.capitalize() capitalizes first character of that word 
#str.endswith("something") it will check that the string is ended with that word or not
#str.replace(old,new)  replaces old with new
#str.find(word)  returns the word of first occurrence
#str.count(word)  returns the count of word in string
Name = "prion"
print(Name.capitalize())  # it will print 'Prion'
print(Name.endswith("n"))  # it will print True
print(Name.replace("p","P"))  # it will print 'Prion'
print(Name.find("r"))  # it will print 1
print(Name.count("i"))  # it will print 1

#---Conditional statements---
#syntax ----> 
# if condition: 
#     print("something")
# elif condition:           #you can write as many elif as you want
#     print("something")
# else:
#     print("something")

#nested conditional statements

#---Ternary operator/single line if---
#syntax ----->  <var> = <var1> if (condition) else <var2>
food =input("food :")
eat = "yes" if food == "cake" else "no"
print(eat) 

#---Ternary operator/clever if---
#syntax ----->  <var> = (false_val,true_val) [(condition)]  
#Note: you can write as many conditions as you want
age = int(input("age:"))
vote = ("no","yes") [age>=18]
print(vote) 









