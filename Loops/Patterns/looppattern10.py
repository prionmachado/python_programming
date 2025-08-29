n = int(input("Enter number:"))

for i in range(1,n+1):
    for j in range(i,n+1):
        print("*",end="")
    print() 

for i in range(n,0,-1):
    for j in range(0,i):
        print("*",end="")
    print() 
