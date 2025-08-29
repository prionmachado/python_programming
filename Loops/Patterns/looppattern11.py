# n = int(input("Enter number:"))
# for i in range(0,n):
#   for j in range(0,n-i-1):
#     print(end=" ")
#   for j in range(0,i+1):
#     print("*",end=" ")
#   print() 

# for i in range(n,0,-1):
#   for j in range(0,n-i):
#     if j == 3:
#       break
#     else:
#       print(end=" ")
#   for j in range(0,i):
#     print("*",end=" ")
#   print() 

n = int(input("Enter number:"))
for i in range(n):
    print(' '*(n-i-1)+'*'*(i+1))
for j in range(n-1,0,-1):
    print(' '*(n-j)+'*'*(j))
