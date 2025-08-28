def isprime(n):
    for i in range (2,n):
        if n%i == 0:
            return 0
    return n

n = int(input("Enter a number:"))
sum1 = 0
while(n>0):
    k = n%10
    sum1 = sum1 + isprime(k)
    n = n//10
print("Sum of Prime digits",sum1) 
     