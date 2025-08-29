Name=input("Enter your name:")
citizenship=int(input("Are you an indian citizen ? type 1 for yes and type 0 for no: "))
if citizenship==1 :
    age=int(input("Ente your age:"))
    if age>=18 :
        print(Name,"is eligible to vote")
    else:
        print(Name,"is not eligible to vote")
elif citizenship==0:
    print(Name,"is not eligible to vote")
else:
    print("invalid input")
