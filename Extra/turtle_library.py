# # # import turtle

# # # t = turtle.Turtle()
# # # t.speed(5)
# # # t.pensize(5)

# # # # --- Draw P ---
# # # t.penup()
# # # t.goto(-300, -100)   # starting position
# # # t.pendown()

# # # t.setheading(90)       
# # # t.forward(200)         # vertical stem
# # # t.right(90)
# # # t.forward(80)          # top horizontal
# # # t.right(90)
# # # t.forward(100)         # right vertical
# # # t.right(90)
# # # t.forward(80)          # middle horizontal

# # # # --- Draw R ---
# # # t.penup()
# # # t.goto(-180, -100)   # move right for R
# # # t.pendown()

# # # t.setheading(90)
# # # t.forward(200)         # vertical stem
# # # t.right(90)
# # # t.forward(80)          # top horizontal
# # # t.right(90)
# # # t.forward(100)         # right vertical
# # # t.right(90)
# # # t.forward(80)          # middle horizontal

# # # # diagonal leg of R
# # # t.penup()
# # # t.goto(-180, 0)        # mid-height of stem
# # # t.pendown()
# # # t.goto(-100, -100)     # diagonal to baseline

# # # # --- Draw I ---
# # # t.penup()
# # # t.goto(-60, -100)      # move right for I
# # # t.pendown()

# # # t.setheading(0)
# # # t.forward(60)          # bottom bar
# # # t.penup()
# # # t.goto(-30, -100)      # center bottom
# # # t.setheading(90)
# # # t.pendown()
# # # t.forward(200)         # vertical line
# # # t.penup()
# # # t.goto(-60, 100)       # top bar start
# # # t.setheading(0)
# # # t.pendown()
# # # t.forward(60)          # top bar

# # # t.hideturtle()
# # # turtle.done()
# # import turtle

# # t = turtle.Turtle()
# # t.speed(5)
# # t.pensize(5)

# # # Draw P
# # t.penup()
# # t.goto(-350, -100)   # starting left
# # t.pendown()

# # t.setheading(90)       
# # t.forward(200)         # vertical stem
# # t.right(90)
# # t.forward(80)          # top horizontal
# # t.right(90)
# # t.forward(100)         # right vertical
# # t.right(90)
# # t.forward(80)          # middle horizontal

# # # Draw R
# # t.penup()
# # t.goto(-180, -100)   # move right for R
# # t.pendown()

# # t.setheading(90)
# # t.forward(200)         # vertical stem
# # t.right(90)
# # t.forward(80)          # top horizontal
# # t.right(90)
# # t.forward(100)         # right vertical
# # t.right(90)
# # t.forward(80)          # middle horizontal

# # # diagonal leg of R
# # t.penup()
# # t.goto(-180, 0)        # mid-height of stem
# # t.pendown()
# # t.goto(-100, -100)     # diagonal to baseline

# # # Draw I
# # t.penup()
# # t.goto(-90, -100)     # move right for I
# # t.pendown()

# # t.setheading(90)
# # t.forward(200)         # vertical line

# # # Draw O
# # t.penup()
# # t.goto(20, -70)        # position for circle (baseline alignment)
# # t.setheading(0)
# # t.pendown()
# # t.circle(70)           # O with radius 70

# # t.hideturtle()
# # turtle.done()
# import turtle

# t = turtle.Turtle()
# t.speed(5)
# t.pensize(5)

# # Draw P
# t.penup()
# t.goto(-370, -100)   # starting left
# t.pendown()

# t.setheading(90)       
# t.forward(200)         # vertical stem
# t.right(90)
# t.forward(80)          # top horizontal
# t.right(90)
# t.forward(100)         # right vertical
# t.right(90)
# t.forward(80)          # middle horizontal

# # Draw R
# t.penup()
# t.goto(-280, -100)   # move right for R
# t.pendown()

# t.setheading(90)
# t.forward(200)         # vertical stem
# t.right(90)
# t.forward(80)          # top horizontal
# t.right(90)
# t.forward(100)         # right vertical
# t.right(90)
# t.forward(80)          # middle horizontal

# # Diagonal leg of R
# t.penup()
# t.goto(-280, 0)       # mid-height of stem
# t.pendown()
# t.goto(-200, -100)    # diagonal down to baseline

# # Draw I
# t.penup()
# t.goto(-140, -100)    # move right for I
# t.pendown()

# t.setheading(90)
# t.forward(200)         # vertical line

# # Draw O
# t.penup()
# t.goto(-40, -70)       # position for O
# t.setheading(0)
# t.pendown()
# t.circle(70)           # O with radius 70

# # Draw N
# t.penup()
# t.goto(140, -100)      # left base of N
# t.pendown()

# t.setheading(90)
# t.forward(200)         # left vertical
# t.goto(220, -100)      # diagonal to bottom right
# t.setheading(90)
# t.forward(200)         # right vertical

# t.hideturtle()
# turtle.done()

import turtle

t = turtle.Turtle()
t.speed(5)
t.pensize(5)

t.penup()
t.goto(-370, -100)
t.pendown()
t.setheading(90)
t.forward(200)
t.right(90)
t.forward(80)
t.right(90)
t.forward(100)
t.right(90)
t.forward(80)

t.penup()
t.goto(-280, -100)
t.pendown()
t.setheading(90)
t.forward(200)
t.right(90)
t.forward(80)
t.right(90)
t.forward(100)
t.right(90)
t.forward(80)
t.penup()
t.goto(-280, 0)
t.pendown()
t.goto(-200, -100)

t.penup()
t.goto(-140, -100)
t.pendown()
t.setheading(90)
t.forward(200)

t.penup()
t.goto(-40, -70)
t.setheading(0)
t.pendown()
t.circle(70)

t.penup()
t.goto(100, -100)
t.pendown()
t.setheading(90)
t.forward(200)
t.goto(220, -100)
t.setheading(90)
t.forward(200)

t.hideturtle()
turtle.done()
