import csv

Name = input("What's your name? ").rstrip()
Home = input("Where's your home? ").rstrip() 

with open("File/fstudent1.csv", "a", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "Home"]) 
    writer.writerow({"Name":Name, "Home":Home}) 

# reader = csv.reader(file)  # reads the file in read mode

# import csv

# with open("File/fstudent1.csv", "a", newline='') as file:
#     writer = csv.writer(file)

#     while True:
#         name = input("What's your name? ").rstrip()
#         if name.lower() == "stop":
#             break
        
#         home = input("Where's your home? ").rstrip() 

#         writer.writerow([name, home])

# print("All entries saved successfully!")