ll=int(input("enter a lower limit"))
ul=int(input("enter a upoer limit"))
even=" "
odd=" "
for i in range(ll,ul+1):
    if i%2==0:
        even+=str(i)+" "
    else:
        odd+=str(i)+" "
print("Even numbers are:",even)
print("Odd numbers are:",odd)
