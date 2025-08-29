#if-elif-else example
light = input("Enter traffic light colour: ")
if(light == "red"):
    print("Stop")
elif(light == "yellow"):
    print("Wait")
elif(light == "green"):
    print("Go")
elif(light == "white"):
    print("Light is broken")
else:
    print("invalid light colour") 

#Another example
marks = int(input("Enter marks: "))
if(marks>=90):
    print("Grade A")
elif(marks<90 and marks>=80):
    print("Grade B")
elif(marks<80 and marks>=70):
    print("Grade C")
else:
    print("Grade D") 