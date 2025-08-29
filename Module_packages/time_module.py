import time 

timestamp = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime()) 
print("Current timestamp:", timestamp) 

if timestamp == "01-01-2023 00:00:00":
    print("Happy New Year!") 
elif timestamp == "25-12-2023 00:00:00":
    print("Merry Christmas!")
elif timestamp == "14-08-2023 00:00:00":
    print("Happy Independence Day!")

timestamp1 = time.strftime("%H:%M:%S", time.localtime())
if "00:00:00" <= timestamp1 <= "12:00:00":
    print("Good Morning!")
elif "12:00:01" <= timestamp1 <= "17:00:00":
    print("Good Afternoon!") 
elif "17:00:01" <= timestamp1 <= "23:59:59":
    print("Good Evening!")
elif "23:59:59" <= timestamp1 <= "00:00:00":
    print("Good Night!") 

# sleep function in time module
# print(4)
# time.sleep(5)
# print("This is printed after 10 seconds") 