import re

def main():
    code = input("Hexadecimal colour code: ").strip() 

    pattern = r"^#[A-Fa-f0-9]{6}$"  
    match = re.search(pattern, code) 
    if match:
        print(f"Valid. Matched with {match.group(0)}")
    else:
        print("Invalid colour code.") 

main() 