#--------------Chapter 3 : Lists and tuples----------------

#---Lists in python---

student = ["Prion",45,78.99]
print(student[0]) # prints "Prion"

# #---Lists are mutable in python---
student[0] = "blaise"
print(student)

# #---Length---
print(len(student))

# #---List slicing---
# #it's similar to string slicing
# #syntax ----> list_name[start:end:step]
print(student[1:3])
print(student[1:3:2])
print(student[0: ]) 

#---List methods---
#list.append() - adds an element to the end of the list
#list.insert() - inserts an element at a specified position
#list.remove() - removes the first occurrence of the element
#list.pop() - removes the element at the specified position
#list.sort() - sorts the list in ascending order
#list.reverse() - reverses the list 
#list.sort(reverse=True) - sorts in descending order
#list.index() - returns the index of the first occurrence of the element
#list.count() - returns the number of occurrences of the element
#list.copy() - returns a copy of the list
# list.clear() - removes all elements from the list

student1 = [1,4,7,3]

student1.append(4)
print(student1)

student1.sort()
print(student1)

student1.insert(1,5)
print(student1)

student1.sort(reverse=True)
print(student1)

student1.reverse()
print(student1)

student1.remove(3)
print(student1)

student1.pop(2)
print(student1) 

student1.count(3)
print(student1) 

student1.copy()
print(student1)

student1.clear()
print(student1) 

#---Tuples in python---
#Tuples are similar to lists but are immutable, meaning they cannot be changed after creation.
marks = ("Prion",1,90.00,1)
print(marks[0]) 

#---Tuple slicing---
#same as list slicing
print(marks[0:3])

#---Tuple methods---
#tuple.index() - returns the index of the first occurrence of the element
#tuple.count() - returns the number of occurrences of the element
#tuple.copy() - returns a copy of the tuple

marks.index(90.00)
print(marks)

marks.count(1)
print(marks) 
