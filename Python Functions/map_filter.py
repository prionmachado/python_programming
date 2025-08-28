def cube(x):
    return x ** 3

print(cube(3)) 

l = [1,2,3,4,5,6,7,8] 

# newl = []
# for i in l:
#     newl.append(cube(i)) 
# print(newl) 

# Using map function
newl = list(map(lambda x:x**3, l))
print(newl) 

#Using filter 
def filter_function(a):
    return a>2  

newnewl = list(filter(filter_function, l))
print(newnewl) 