p = 1
n = int(input("Enter the number:"))
for i in range(2,n):
    if(n%2 == 0):
        p = 0
        break
if (p == 1):
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")
    