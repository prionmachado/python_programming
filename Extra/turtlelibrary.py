import turtle

t = turtle.Turtle()
t.speed(6)
t.pensize(5)

# layout
baseline = 0
h = 120        # letter height
w = 40         # loop width for P/R
spacing = 120  # advance between letters
diag_len = 70  # R diagonal length
o_radius = 30
i_width = 30
n_width = 70

def draw_P(x):
    t.penup(); t.goto(x, baseline); t.setheading(90); t.pendown()
    t.forward(h)
    t.right(90); t.forward(w)
    t.right(90); t.forward(h/2)
    t.right(90); t.forward(w)
    t.penup(); t.setheading(0)

def draw_R(x):
    # stem + loop (same shape as P)
    t.penup(); t.goto(x, baseline); t.setheading(90); t.pendown()
    t.forward(h)
    t.right(90); t.forward(w)
    t.right(90); t.forward(h/2)
    t.right(90); t.forward(w)
    t.penup()
    # diagonal leg starts at right edge of loop (mid height) and goes to baseline
    start_x = x + w
    start_y = baseline + h/2
    end_x = start_x + diag_len
    end_y = baseline
    t.goto(start_x, start_y)
    t.pendown()
    t.goto(end_x, end_y)
    t.penup(); t.setheading(0)

def draw_I(x):
    # top bar
    t.penup(); t.goto(x - i_width/2, baseline + h); t.setheading(0); t.pendown()
    t.forward(i_width)
    # stem
    t.penup(); t.goto(x, baseline); t.setheading(90); t.pendown()
    t.forward(h)
    # bottom bar
    t.penup(); t.goto(x - i_width/2, baseline); t.setheading(0); t.pendown()
    t.forward(i_width)
    t.penup(); t.setheading(0)

def draw_O(x):
    # left bound x, circle centered at x + r
    cx = x + o_radius
    cy = baseline + o_radius
    t.penup(); t.goto(cx + o_radius, cy); t.setheading(90); t.pendown()
    t.circle(o_radius)
    t.penup(); t.setheading(0)

def draw_N(x):
    # left vertical
    t.penup(); t.goto(x, baseline); t.setheading(90); t.pendown()
    t.forward(h)
    # diagonal from top-left to bottom-right
    t.penup(); t.goto(x, baseline + h); t.pendown()
    t.goto(x + n_width, baseline)
    # right vertical
    t.penup(); t.goto(x + n_width, baseline); t.setheading(90); t.pendown()
    t.forward(h)
    t.penup(); t.setheading(0)

# draw PRION
x = -260
draw_P(x); x += spacing
draw_R(x); x += spacing
draw_I(x); x += spacing
draw_O(x); x += spacing
draw_N(x)

t.hideturtle()
turtle.done()
