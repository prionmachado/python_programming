while True:
    try:
        a = int(input("Enter first number: "))
        break
    except:
        pass
while True:
    try:
        b = int(input("Enter second number: "))
        if b == 0:
            continue
        break
    except ValueError:
        pass

ans = input("Enter operation name: ") 
if ans=="+":
    print(a+b)
elif ans=="-":
    print(a-b)
elif ans=="*":
    print(a*b)
elif ans=="/":
    print(a/b)
else:
    print("Invalid")
