#type conversion

#simple conversion
a = 2
b = 4.25

sum = a + b # 2.0 + 4.25 => 6.25
print(sum)

#type casting
a,b = 1, "2"
c = int(b)  #here we are converting string "2" to int and this is called type casting(forced conversion).
sum = a + c 
print(sum) 