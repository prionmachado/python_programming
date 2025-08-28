n = int(input("How many times do you want to write your name? "))

file = open("File/file.txt", "a")

for i in range(n):
    name = input("What's your name? ")
    file.write(f"{name}\n")

file.close()  