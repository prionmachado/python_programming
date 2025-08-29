# WAP to create user defined list and generate a prime list from the given list

def isprime(n):
    for i in range (2,n):
        if n%i == 0:
            return 0
    return 1

n = int(input("Enter the number of elements:"))
l = []
prime = []
for i in range (1,n+1):
    l.append(int(input("Enter the element:")))
print("Original list",l) 

for i in l:
    if(isprime(i) == 1):
        prime.append(i)
print("Prime list",prime)  