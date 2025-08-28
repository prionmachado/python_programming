#import turtle

#t = turtle.Turtle()
# t.pensize(5)
# t.speed(3)

# t.penup()
# t.goto(-50, -50)
# t.pendown()
# t.left(90)
# t.forward(100)

# t.right(90)
# t.circle(-25, 180)

# t.hideturtle()
# turtle.done()
# t.goto(-50, -50)
# t.pensize(5)
# t.speed(10)
# t.left(90)
# t.forward(250)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.home()
# t.goto(-60, -60)
# t.left(90)
# t.forward(250)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.home()
# t.goto(-70, -70)
# t.left(90)
# t.forward(250)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)

# t.left(90)
# t.forward(100)  # Vertical line
# t.right(90)
# t.forward(50)   # Top horizontal line
# t.right(90)
# t.forward(50)   # Middle vertical line
# t.right(90)
# t.forward(50)  

import turtle

t = turtle.Turtle()
t.pensize(5)
t.speed(3)

# Function to move without drawing
def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Draw 'P'
move_to(-200, 50)
t.left(90)
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)

# Draw 'R'
move_to(-120, 150)
t.left(90)
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.left(135)
t.forward(70)
t.right(45) 

# Draw 'I'
move_to(-30, 50)
t.forward(50)
move_to(-5, 50)
t.right(90)
t.forward(100)
move_to(-30, -50)
t.forward(50)

# Draw 'O'
move_to(50, 0)
t.circle(30)

# Draw 'N'
move_to(120, -50)
t.left(90)
t.forward(100)
t.goto(180, -50)
t.goto(180, 50)

t.hideturtle()
turtle.done()
