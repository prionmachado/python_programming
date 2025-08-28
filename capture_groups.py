import re 

locations = {"+1": "United States and Canada","+62": "Indonesia", "+505": "Nicaragua"}

def main():
    pattern = r"(?P<country_code>\+\d{1,3})(?P<phone_number> \d{3}-\d{3}-\d{4})"
    number = input("Number: ").strip()

    match = re.search(pattern, number)

    if match:
        country_code = match.group("country_code") 
        phone_number = match.group("phone_number")
        print(f"Country code: {country_code}")
        print(f"Phone number: {phone_number}") 
        print(f"Country: {locations[country_code]}")
        print("Valid")
    else:
        print("Invalid") 

main() 