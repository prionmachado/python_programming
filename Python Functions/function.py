#function definition
def add(a=1,b=1):  #a,b are parameters   
    s=a+b
    return s

a = int(input("Enter number:"))
b = int(input("Enter number:"))

#function call
print(add(3,5))  #a,b are arguments


def print_hello():
    print("Hello")  #no parameters no return values is possible

output = print_hello()
print(output)  #none