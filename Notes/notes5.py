#-----------------Chapter 6 : Functions and Recursion-------------

#---Functions in python---

#syntax ----> 
# def func_name(para1,para2......):    |
#       some work                      | ----- Function definition
#       return value                   |

#func_name(arg1,arg2....)     --- Function call

def printInDecreasing(x):
    while(x >= 0):
        print(x,end=" ")
        x-=1
x = int(input("Enter:"))
printInDecreasing(x) 