#raising exceptions 

def main():
    miles = float(input("Enter miles: "))
    minutes = int(input("Enter minutes: "))
    pace = get_pace(miles, minutes)
    print(f"You need to run each mile in {round(pace,2)} minutes.")

def get_pace(miles,minutes):
    if miles <= 0:
        raise ValueError("Miles must be greater than 0.")
    if minutes <= 0:
        raise ValueError("Minutes must be greater than 0.")
    pace = minutes / miles
    return pace

main() 