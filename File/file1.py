names = []

with open("File/file.txt", "r") as file:  # open opens and closes the file automatically
    # lines = file.readlines() # Read all lines at once
    for line in file:
        names.append(line.strip()) 

for name in sorted(names, reverse=True):
    print(f"Hello, {name}!") 

# strip = removes newlines,spaces from both left and right
# rstrip = removes newlines,spaces from right side only
# lstrip = removes newlines,spaces from left side only 