Name=input("Enter your name:")
income=int(input("Enter your income:"))
if income<=300000:
    tax=0
elif income <=600000:
    tax=600000*0.05
elif income<=900000:
    tax=30000+((income-600000)*0.1)
elif income<=1200000:
    tax=120000+((income-900000)*0.15)
elif income<= 1500000:
    tax=300000+((income-1200000)*0.2)
else:
    tax=600000+((income-1500000)*0.3)
print("Tax is",tax)
