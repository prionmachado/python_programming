a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

if (a == b == c):
    print("All are equal numbers")
elif (a>=b and a>=c):
    print(a,"is greatest than",b,"and",c) 
elif(b>=c):
    print(b,"is greatest than",a,"and",c)
else:
    print(c,"is greatest than",b,"and",a)
    