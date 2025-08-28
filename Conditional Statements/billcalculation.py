Name=input("Enter your name:")
units=int(input("Enter your units consumed:"))
if units<=50:
   bill=units*0.5
elif units <=100:
   bill=25+((units-50)*0.75)
elif units<=250:
   bill=100+((units-150)*1.2)
else:
    bill=220+((units-250)*1.5)
totalbill=(bill*0.2)+bill
print("Bill is",bill)
print("Total Bill is",totalbill) 