marks = [34,67,98,23,1,0] 
for index, mark in enumerate(marks):
    print(index, mark) 

print("==============================")
#changing the start index
marks = [34,67,98,23,1,0] 
for index, mark in enumerate(marks, start=1):
    print(index, mark) 