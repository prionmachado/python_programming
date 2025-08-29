from word2number import w2n

def words_to_number():
    text = input("Enter a number in words: ") 
    try:
        num = w2n.word_to_num(text)  
        print(f"Output: {num:,}")
    except ValueError:
        print("Invalid input. Please enter a valid number in words.")

words_to_number() 