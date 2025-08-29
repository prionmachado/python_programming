n = int(input("Enter number:"))
for i in range(1,n+1):
    print(" " * (n-i),end="")     #end="" the default one line spacing is not given
    print("*" * (2*i-1),end="")
    print() 

num = int(input("Enter number:"))
for i in range(0,num):
  for j in range(0,num-i-1):
    print(end=" ")
  for j in range(0,i+1):
    print("*",end=" ")
  print() 

n = int(input("Enter number:"))
for i in range(n,0,-1):
  for j in range(0,n-i):
    print(end=" ")
  for j in range(0,i):
    print("*",end=" ")
  print() 
