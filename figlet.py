import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    if (
        len(sys.argv) == 3
        and (sys.argv[1] == "-f" or sys.argv[1] == "--font")
        and sys.argv[2] in fonts
    ):
        figlet.setFont(font=sys.argv[2])
    elif len(sys.argv) == 1:
        font = random.choice(figlet.getFonts())
        figlet.setFont(font=font)
    else:
        sys.exit("Invalid arguments")

    f = input("Input: ")
    if not f.strip():
        print("Invalid input")
    else:
        print("Output:")
        print(figlet.renderText(f))

if __name__ == "__main__":
    main() 