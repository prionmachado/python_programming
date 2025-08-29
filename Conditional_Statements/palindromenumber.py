# def reverse(n):
#     rev = 0
#     while(n>0):
#         k = n%10
#         rev = rev*10+k
#         n = n//10
#     return rev
# n = int(input("Enter a number:"))
# if (n == reverse(n)):
#     print("Palindrome")
# else:
#     print("Not palindrome") 
    
n = int(input("Enter a number:"))
reversed = 0

for num in str(n):
    reversed = reversed * 10 + int(num)
if n == reversed:
    print("Palindrome") 
else:
    print("Not palindrome") 

