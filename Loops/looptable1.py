n = int(input("Enter number:"))
if n>0:
    for i in range(1,11):
        print(n,"*",i,"=",n*i)   #print(n*i) 
else:
    print("Negative numbers are not allowed")
    