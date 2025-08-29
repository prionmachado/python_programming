n = int(input("Enter number:"))

for i in range(n+1,1,-1):
    for j in range(i,1,-1):
        print("*",end="")
    print() 