#ValueError
#If try runs successfully, the except block is skipped and the else is executed.
#If an exception occurs, the except block is executed and the else block is skipped.

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while(True):
        try:
            num = int(input("Enter number: "))
        except ValueError:
            pass
            # print("x is not an integer") 
        else:
            return num

if __name__ == "__main__":
    main() 