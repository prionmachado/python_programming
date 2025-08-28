# WAP program to pick the smallest and largest number from a given list

n = int(input("Enter the number of elements:"))
l = []
for i in range (1,n+1):
    l.append(int(input("Enter the element:"))) 
print("Original list",l)

l.sort()    

print("The smallest number is",l[0])
print("The largest number is",l[n-1]) 