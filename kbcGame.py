import pygame
import sys

pygame.init()

# Screen setup
WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("KBC - Kaun Banega Crorepati")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)
DARK_GRAY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Fonts
font = pygame.font.SysFont(None, 28)
big_font = pygame.font.SysFont(None, 40)
title_font = pygame.font.SysFont(None, 52)

clock = pygame.time.Clock()

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

class Button:
    def __init__(self, x, y, w, h, text, color=GRAY, hover_color=DARK_GRAY):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.color = color
        self.base_color = color
        self.hover_color = hover_color
        self.hovered = False

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=5)
        text_surf = font.render(self.text, True, BLACK)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def update(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.color = self.hover_color
            self.hovered = True
        else:
            self.color = self.base_color
            self.hovered = False

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

def draw_text(surface, text, font, color, x, y, wrap_width=None):
    """Draw text, optionally wrapped to fit in wrap_width"""
    if wrap_width is None:
        text_surface = font.render(text, True, color)
        surface.blit(text_surface, (x, y))
        return font.size(text)[1]

    words = text.split(' ')
    lines = []
    current_line = ""
    for word in words:
        test_line = current_line + word + " "
        if font.size(test_line)[0] > wrap_width:
            lines.append(current_line)
            current_line = word + " "
        else:
            current_line = test_line
    lines.append(current_line)

    height = 0
    for line in lines:
        text_surface = font.render(line, True, color)
        surface.blit(text_surface, (x, y + height))
        height += font.get_height()
    return height

def main():
    question_index = 0
    running = True
    selected_option = None
    feedback = ""
    show_feedback = False
    lifelines = {"5050": True, "hint": True, "skip": True}
    used_5050 = False
    money_won = 0
    options_to_show = []  # options after 50-50 use
    hint_text = ""

    # Buttons positions
    btn_width = 380
    btn_height = 50
    gap = 20
    start_x = 60
    start_y = 300

    # Lifeline buttons
    lifeline_buttons = {
        "5050": Button(700, 150, 150, 40, "50-50"),
        "hint": Button(700, 210, 150, 40, "Hint"),
        "skip": Button(700, 270, 150, 40, "Skip")
    }

    # Option buttons, will be created fresh each question
    def create_option_buttons(opts):
        btns = []
        for i, opt in enumerate(opts):
            btn = Button(start_x, start_y + i*(btn_height+gap), btn_width, btn_height, opt)
            btns.append(btn)
        return btns

    # Initialize buttons for first question
    options_to_show = questions[question_index]["options"]
    option_buttons = create_option_buttons(options_to_show)

    while running:
        mouse_pos = pygame.mouse.get_pos()

        screen.fill(WHITE)

        # Title
        draw_text(screen, "KBC - Kaun Banega Crorepati", title_font, BLUE, 30, 20)

        # Show money won so far
        draw_text(screen, f"Money Won: ₹ {money_won:,}", big_font, BLACK, 30, 80)

        # Show question number and question text (wrapped)
        question_text = questions[question_index]["question"]
        draw_text(screen, question_text, big_font, BLACK, 30, 130, wrap_width=600)

        # Draw option buttons and update hover color
        for btn in option_buttons:
            btn.update(mouse_pos)
            btn.draw(screen)

        # Draw lifeline buttons
        for key, lifeline_btn in lifeline_buttons.items():
            lifeline_btn.update(mouse_pos)
            # Gray out if used
            if not lifelines[key]:
                lifeline_btn.color = DARK_GRAY
            lifeline_btn.draw(screen)

        # Show hint if used
        if hint_text:
            draw_text(screen, f"Hint: {hint_text}", font, RED, 30, 550, wrap_width=840)

        # Show feedback for answer selection
        if show_feedback:
            color = GREEN if feedback == "Correct!" else RED
            draw_text(screen, feedback, big_font, color, 30, 600)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                # Check lifeline clicks
                for key, lifeline_btn in lifeline_buttons.items():
                    if lifeline_btn.is_clicked(pos) and lifelines[key]:
                        if key == "5050" and not used_5050:
                            # Show only 2 options: correct + one wrong
                            used_5050 = True
                            lifelines["5050"] = False
                            correct = questions[question_index]["answer"]
                            # The 50-50 options are in the question data:
                            options_to_show = questions[question_index]["5050"]
                            option_buttons = create_option_buttons(options_to_show)
                            hint_text = ""
                            selected_option = None
                            show_feedback = False

                        elif key == "hint" and lifelines["hint"]:
                            lifelines["hint"] = False
                            hint_text = questions[question_index]["hint"]
                            selected_option = None
                            show_feedback = False

                        elif key == "skip" and lifelines["skip"]:
                            lifelines["skip"] = False
                            # Skip to next question as if answered correctly
                            money_won = questions[question_index]["money"]
                            question_index += 1
                            if question_index >= len(questions):
                                # Game won
                                feedback = "Congratulations! You won the game!"
                                show_feedback = True
                                option_buttons = []
                            else:
                                options_to_show = questions[question_index]["options"]
                                option_buttons = create_option_buttons(options_to_show)
                                used_5050 = False
                                hint_text = ""
                                selected_option = None
                                show_feedback = False
                        break

                # Check option buttons clicked only if no feedback is showing
                if not show_feedback:
                    for i, btn in enumerate(option_buttons):
                        if btn.is_clicked(pos):
                            selected_option = i
                            # Get letter of selected option, e.g. "A", "B"...
                            selected_letter = btn.text[0]
                            correct_letter = questions[question_index]["answer"]

                            if selected_letter == correct_letter:
                                feedback = "Correct!"
                                money_won = questions[question_index]["money"]
                            else:
                                feedback = f"Wrong! Correct answer was {correct_letter}."
                                money_won = 0  # Lose everything

                            show_feedback = True
                            break

            # Advance to next question after showing feedback and click anywhere
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                if show_feedback:
                    if feedback.startswith("Wrong") or question_index == len(questions)-1 and feedback == "Correct!":
                        # Game over (lost or finished all questions)
                        running = False
                    elif feedback == "Correct!":
                        # Next question
                        question_index += 1
                        if question_index >= len(questions):
                            feedback = "Congratulations! You won the game!"
                            show_feedback = True
                            option_buttons = []
                        else:
                            options_to_show = questions[question_index]["options"]
                            option_buttons = create_option_buttons(options_to_show)
                            used_5050 = False
                            hint_text = ""
                            selected_option = None
                            show_feedback = False

        pygame.display.flip()
        clock.tick(30)

    # Show final screen for 3 seconds then quit
    screen.fill(WHITE)
    if money_won > 0:
        draw_text(screen, f"Game Over! You won ₹ {money_won:,}", big_font, GREEN, 100, 300)
    else:
        draw_text(screen, "Game Over! Better luck next time.", big_font, RED, 100, 300)
    pygame.display.flip()
    pygame.time.wait(3000)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
