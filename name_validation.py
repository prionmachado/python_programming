import re

name = input("Enter your name: ").strip()
if matches := re.search(r"^(.+), *(.+)$", name):
    # last = matches.group(1)
    # first = matches.group(2)
    name = matches.group(2) + " " + matches.group(1)
print(f"Hello {name}!")

# input = Prion Machado Output = Hello Prion Machado cause there is no comma
# input = Machado, Prion Output = Hello Prion Machado cause there is a comma
# it formatted the name to be first last

# walrus operator := is used to assign a value from right to left and also do the if statement
