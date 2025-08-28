# Question 1
# list1 = [1,2,3], [4,5,6], [7,8,9]
# list2 = [3,7,1],[2,9,6],[3,1,5]
# list3 = [[0,0,0],[0,0,0],[0,0,0]] 
# print("Original list",list1)
# print("Original list",list2)

# for i in range(0,len(list1)):
#     for j in range(0,len(list1)):
#         list3[i][j] = list1[i][j] + list2[i][j]
# print("After multiplication ",list3) 

# Question 2
# n = int(input("Enter how many sublist:"))
# l = []
# for i in range(0,n):
#     l.append([]) 

# for i in range(0,len(l)):
#     k = int(input(f"Enter how many elements you want in sublist {i+1}:"))
#     for j in range(0,k):
#         l[i].append(int(input(f"Enter the element {i+1}:")))  
# print(l) 

# Question 3
n = int(input("Enter the number:")) 
limit = int(input("Enter limit:"))
l = []

for i in range(0,n):
    l.append([]) 

for i in range(0,n):
    k = int(input(f"Enter the number for table {i+1}:"))
    for j in range(1,limit+1):
        l[i].append(k * j) 
print(l) 
#This is infinite loop solve it 