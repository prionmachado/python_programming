#wap to check if a list contains a palindrome of elements.

list1 = []
n = int(input("Enter the number of elements:")) 
for i in range(1,n+1):
    list1.append(input("Enter the element:"))
print("Original list",list1) 

copy_list1 = list1.copy() 
copy_list1.reverse()
print("Reversed list",copy_list1) 

# Check if the reversed list is equal to the original list
if copy_list1 == list1: 
    print("Palindrome")
else:
    print("Not Palindrome")  