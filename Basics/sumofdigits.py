n=int(input("enter a number:"))
sum1=0
#while(n>0):
 #   r=n%10
  #  sum1=sum1+r
   # n=n//10
#print("Sum of number is:",sum1)

for num in str(n):
    sum1+=int(num) 
print(sum1)