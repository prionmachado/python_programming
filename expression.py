#Expression execution

#string and numeric values can operate with *
A,B = 2,3
Txt = "@"
print(2*Txt*3)

#string and string can operate with +
a,b = "4",6
txt = "@"
print((a+txt)*b)

#Numeric values can operate with all arithmetic operators
c,d = 3,6
e=4
print(c+d*e)

#Arithmetic expression with integer and float will result in float 
x,y = 10, 5.0
z=x*y
print(z) 

#Result of division operator with two integers will be float 
l,m = 1,2
n = l/m
print(n)

#Integer division with float and int will give int displayed as float
e,f = 1.5,3
g = e//f
print(g,e/f)

#Remainder is negative when denominator is negative 
m,n = 5,-2
o = m%n
print(o) 


