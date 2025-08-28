#Difference between is and == . Both are comparison operators 

a = 5
b = 6

print(a is b) #checks exact location in memory
print(a == b) #checks if the values are equal

a = [1,2,3]
b = [1,2,3] 

print(a is b) 
print(a == b) 

a = (1,2)
b = (1,2)

print(a is b)
print(a == b)
#Why did they both gave true , "is" should give false right ??
#cause tuples are immutable their values does not change 
# that's why "is" gave true 

a = {1,2}
b = {1,2} 

print(a is b) 
print(a == b) 