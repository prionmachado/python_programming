#--------------------Chapter 5 : Loops in python---------------------

#---While loop---

#syntax ----->
# while condition:
#     code to be executed

a = 2
while(a!=0):
    print(a)
    a-=1

# Break
# Continue
# Pass

#---For loop---
# syntax ------> for variable in iterable:
#                     code to be executed
list = [1,2,3]
for i in list:
    print(i)

#---for loop with else--- 
# syntax ------> for variable in iterable:
#                     code to be executed
#                else:
#                     code to be executed when loop ends 

#---Range---
#syntax ----> for i in range(start,stop,step):    step is optional
#                  print(i)
for i in range(1,10,2):
    print(i) 
