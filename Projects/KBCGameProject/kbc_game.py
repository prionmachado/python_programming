questions = [
   {
        "question": "1. What is the capital city of Canada?",
        "options": ["A. Toronto", "B. Ottawa", "C. Vancouver", "D. Montreal"],
        "answer": "B",
        "5050": ["A. Toronto", "B. Ottawa"],
        "hint": "It's located in the province of Ontario.",
        "money": 1000
    },
    {
        "question": "2. Which element has the atomic number 1?",
        "options": ["A. Oxygen", "B. Hydrogen", "C. Helium", "D. Nitrogen"],
        "answer": "B",
        "5050": ["B. Hydrogen", "C. Helium"],
        "hint": "It's the lightest and most abundant element in the universe.",
         "money": 2000
    },
    {
        "question": "3. Which country gifted the Statue of Liberty to the USA?",
        "options": ["A. England", "B. Germany", "C. France", "D. Italy"],
        "answer": "C",
        "5050": ["B. Germany", "C. France"],
        "hint": "It was a gesture of friendship after the American Revolution.",
         "money": 4000
    },
    {
        "question": "4. Which luxury car brand is owned by Tata Motors of India?",
        "options": ["A. Mercedes-Benz", "B. Jaguar", "C. BMW", "D. Ferrari"],
        "answer": "B",
        "5050": ["B. Jaguar", "C. BMW"],
        "hint": "It's a British brand now owned by an Indian company.",
        "money": 8000
    },
    {
        "question": "5. Which country is the car brand 'Toyota' from?",
        "options": ["A. South Korea", "B. China", "C. Japan", "D. Germany"],
        "answer": "C",
        "5050": ["A. South Korea", "C. Japan"],
        "hint": "This country is known for both samurai and high-tech vehicles.",
        "money": 16000
    },
    {
        "question": "6. Which is the longest river in the world?",
        "options": ["A. Amazon", "B. Nile", "C. Yangtze", "D. Mississippi"],
        "answer": "B",
        "5050": ["A. Amazon", "B. Nile"],
        "hint": "It flows through Egypt.",
        "money": 32000
    },
    {
        "question": "7. Which company owns Instagram and WhatsApp?",
        "options": ["A. Apple", "B. Meta", "C. Google", "D. Microsoft"],
        "answer": "B",
        "5050": ["B. Meta", "C. Google"],
        "hint": "It was formerly known as Facebook Inc.",
        "money": 64000
    },
     {
        "question": "8. Which company developed the Android operating system?",
        "options": ["A. Samsung", "B. Google", "C. Microsoft", "D. Apple"],
        "answer": "B",
        "5050": ["B. Google", "D. Apple"],
        "hint": "This company also owns YouTube.",
        "money": 128000
    },
    {
        "question": "9. Which is the smallest bone in the human body?",
        "options": ["A. Stapes", "B. Femur", "C. Ulna", "D. Tibia"],
        "answer": "A",
        "5050": ["A. Stapes", "C. Ulna"],
        "hint": "It's located in the ear.",
        "money": 256000
    },
    {
        "question": "10. Which company produces the iPhone?",
        "options": ["A. Microsoft", "B. Apple", "C. Google", "D. Huawei"],
        "answer": "B",
        "5050": ["A. Microsoft", "B. Apple"],
        "hint": "It's headquartered in Cupertino, California.",
        "money": 512000
    },
    {
        "question": "11. Which organ purifies our blood?",
        "options": ["A. Heart", "B. Lungs", "C. Liver", "D. Kidneys"],
        "answer": "D",
        "5050": ["A. Heart", "D. Kidneys"],
        "hint": "There are two of them and they filter waste.",
        "money": 1024000
    },
    {
        "question": "12. Which is the largest desert in the world?",
        "options": ["A. Gobi", "B. Sahara", "C. Kalahari", "D. Antarctic Desert"],
        "answer": "D",
        "5050": ["B. Sahara", "D. Antarctic Desert"],
        "hint": "It's icy, not sandy.",
        "money": 2048000
    },
    {
        "question": "13. What is the chemical symbol for Gold?",
        "options": ["A. Go", "B. Gl", "C. Au", "D. Ag"],
        "answer": "C",
        "5050": ["C. Au", "D. Ag"],
        "hint": "It comes from the Latin word 'Aurum'.",
        "money": 4096000
    },
    {
        "question": "14. Which Mughal emperor built the Taj Mahal?",
        "options": ["A. Akbar", "B. Humayun", "C. Jahangir", "D. Shah Jahan"],
        "answer": "D",
        "5050": ["A. Akbar", "D. Shah Jahan"],
        "hint": "He built it in memory of Mumtaz Mahal.",
        "money": 8192000
    },
    {
        "question": "15. What is the full form of HTTP?",
        "options": ["A. Hyper Text Transfer Protocol", "B. Hyper Type Text Protocol", "C. High Transfer Text Protocol", "D. Hyper Transfer Test Process"],
        "answer": "A",
        "5050": ["A. Hyper Text Transfer Protocol", "C. High Transfer Text Protocol"],
        "hint": "It's the protocol behind the web.",
        "money": 16384000
    },
    {
        "question": "16. Which Indian state has the highest population?",
        "options": ["A. Maharashtra", "B. Tamil Nadu", "C. Uttar Pradesh", "D. Bihar"],
        "answer": "C",
        "5050": ["A. Maharashtra", "C. Uttar Pradesh"],
        "hint": "It includes cities like Lucknow and Varanasi.",
        "money": 32768000
    },
    {
        "question": "17. Which company created the Windows operating system?",
        "options": ["A. IBM", "B. Microsoft", "C. Intel", "D. Oracle"],
        "answer": "B",
        "5050": ["A. IBM", "B. Microsoft"],
        "hint": "Founded by Bill Gates and Paul Allen.",
        "money": 65536000
    },
    {
        "question": "18. Which of these companies is known for cloud services called AWS?",
        "options": ["A. Apple", "B. Amazon", "C. Adobe", "D. Alphabet"],
        "answer": "B",
        "5050": ["B. Amazon", "C. Adobe"],
        "hint": "Its founder also owns Blue Origin.",
        "money": 130000000 
    }
]  

print("\n==================================================================")
print("--------Welcome to KBC(Kaun Banega Crorepati !!)--------") 
print("==================================================================")

print("\n","Instructions: ")
print("1. Answer the questions by entering A, B, C, or D.")
print("2. You can quit anytime by entering Q.")
print("3. Use L for lifelines.(U have only 3 liflines so use it wisely)\n") 

lifelines_used = [] 
current_earnings = 0

for q in questions:
    print(q["question"])
    for option in q["options"]:
        print(option)
    
    while True:
        answer = input("Your answer (A/B/C/D), 'L' for liflines, or 'Q' to quit: ").strip().upper()
        
        if answer in ["A","B","C","D"]:
            if answer == q["answer"]:
                print(f"\nCorrect! , You won {q['money']:,}\n") 
                current_earnings = q["money"]  
                break
            else:
                print("Wrong answer !! Game Over !!!") 
                print(f"Thanks for playing! You won {current_earnings:,}")  
                exit() 

        elif answer == "Q":
            print(f"Thanks for playing! You won {current_earnings:,}")   
            exit() 

        elif answer == "L":
            available_lifelines = []

            if "5050" not in lifelines_used:
                available_lifelines.append("1. 50-50")
            if "hint" not in lifelines_used:
                available_lifelines.append("2. Give Strong Hint")
            if "skip" not in lifelines_used:
                available_lifelines.append("3. Skip the Question")

            if not available_lifelines:
                print("No lifelines remaining.")
                continue

            print("\nAvailable Lifelines:")
            for lifeline in available_lifelines:
                print(lifeline) 
    
            try:
                lifeline_choice = int(input("Choose a lifeline (1/2/3): "))
            except:
                print("Type 1,2 or 3")
                continue 

            if lifeline_choice == 1 and "5050" not in lifelines_used:
                print("\n---50-50 Lifeline Activated!---")
                for opt in q["5050"]:
                    print(opt) 
                lifelines_used.append("5050")

            elif lifeline_choice == 2 and "hint" not in lifelines_used:
                print("\n---Strong Hint Lifeline Activated!---") 
                print(q["hint"]) 
                lifelines_used.append("hint")

            elif lifeline_choice == 3 and "skip" not in lifelines_used:
                print("\n---Skip Lifeline Activated!---") 
                print("\nQuestion Skipped!\n")
                lifelines_used.append("skip")
                break
            else:
                print("Invalid or already used lifeline. Try again !") 
        else:
            print("Invalid Input")  
print("==============================================================")
print(f" Thanks for playing! You won {current_earnings:,}") 
print("==============================================================\n")
print("\n--------------- Game completed !!! ---------------")  