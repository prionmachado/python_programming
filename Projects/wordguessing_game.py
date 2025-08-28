def level1():
    words = {
        "PAIR" : 4,
        "CHIP" : 2,
        "HAIR" : 3,
        "SINOY" : 5,
        "CHAIR" : 2,
        "PRION" : 8,
        "COIN" : 1,
        "PAIN" : 6,
        "PIANO" : 6,
        "RION" : 3,
    }
    original_words = list(words.keys()) 
    print()
    print("==========================================")
    print("Your LETTERS are : A I N O P R C H S Y") 
    print()
    print("HINT : Words are of 4 or more letters ")
    print("==========================================")
    print() 
    game = input("Enter start or quit: ").lower()
    score = 0
    if game=="start":
        while len(words)>0:
            print()
            print(f"{len(words)} words left!")
            print()
            guess = input("Guess a word: ").upper() 

            if guess in words.keys():
                points = words[guess]
                words.pop(guess)
                score += points
                print()
                print(f"Correct! You got {points} points!")
                print("YOUR SCORE:",score) 
            else:
                print("Wrong! Try again!")
                score -= 1
                print("Your Score:",score) 
        print()
        if score>=35:
            print("Congratulations! You have won the game!")
        else:
            print("You have lost the game!")
        print()
        print("The words were : ",original_words)
    else:
        print("You have quit the game!")


def level2():
    words = {
        "CAMERA" : 5,
        "MAGNET" : 2,
        "RANDOM" : 2,
        "MENTOR" : 4,
        "ROMANCE" : 4,     
        "TORNADO" : 3,
        "DRAGON" : 3,
        "DANCE" : 7,
        "GARDEN" : 8,
        "CANTEEN" : 3,
    }
    original_words = list(words.keys()) 
    print()
    print("============================================")
    print("Your LETTERS are :  C M N A T R D O G E") 
    print()
    print("HINT : Words are of 5 or more letters.")
    print("============================================")
    print() 
    game = input("Enter start or quit: ").lower()
    score = 0

    if game=="start":
        while len(words)>0:
            print()
            print(f"{len(words)} words left!")
            print()
            guess = input("Guess a word: ").upper() 

            if guess in words.keys():
                points = words[guess]
                words.pop(guess)
                score += points
                print()
                print(f"Correct! You got {points} points!")
                print("YOUR SCORE:",score) 
            else:
                print("Wrong! Try again!")
                score -= 1
                print("Your Score:",score) 
        print()
        if score>=35:
            print("Congratulations! You have won the game!")
        else:
            print("You have lost the game!")
        print()
        print("The words were : ",original_words)
    else:
        print("You have quit the game!")

def level3():
    words = {
        ...
    }
    original_words = list(words.keys()) 
    print()
    print("============================================")
    print("Your LETTERS are :  ") 
    print()
    print("HINT : Words are of 5 or more letters.")
    print("============================================")
    print() 
    game = input("Enter start or quit: ").lower()
    score = 0

    if game=="start":
        while len(words)>0:
            print()
            print(f"{len(words)} words left!")
            print()
            guess = input("Guess a word: ").upper() 

            if guess in words.keys():
                points = words[guess]
                words.pop(guess)
                score += points
                print()
                print(f"Correct! You got {points} points!")
                print("YOUR SCORE:",score) 
            else:
                print("Wrong! Try again!")
                score -= 1
                print("Your Score:",score) 
        print()
        if score>=35:
            print("Congratulations! You have won the game!")
        else:
            print("You have lost the game!")
        print()
        print("The words were : ",original_words)
    else:
        print("You have quit the game!")

def main():
    print() 
    print("------- Welcome to the Word Guessing Game! -------")
    print()
    print("========================= RULES =======================")
    print("1. You have to guess 10 words using the letters.")
    print("2. Points will be given according to your word!")
    print("3. Minus 1 for every wrong guess!")
    print("4. You need 35 points to win!")
    print("=======================================================")
    print()
    level = input("Enter difficulty (easy/hard): ").lower()

    if level=="easy":
        level1()
    elif level=="hard":
        level2()    
    else:
        print("Invalid Input!") 

if __name__ == "__main__":
    main()
