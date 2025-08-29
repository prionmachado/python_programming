#Search for a number x in this tuple using loop: [1,4,9,16,25,36,49,64,81,100]

num = [1,4,9,16,25,36,49,64,81,100]
x = 36
i = 0
while i < len(num):
    if (num[i] == x):
        print("Number found at index", i)
    else :
        print("finding.....")
    i += 1
    
