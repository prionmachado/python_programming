import re

email = input("What's your email address? ").strip()

if re.search(r"^\w+@\w+\.(com|edu|in)$",email):
    print("Valid")
else:
    print("Invalid")

# re.IGNORECASE will ignore the case of the letters in the email address.
