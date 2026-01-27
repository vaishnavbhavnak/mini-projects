import turtle
import math
import time

WIDTH, HEIGHT = 800, 600
SAFFRON = "#FF9933"
WHITE = "#FFFFFF"
GREEN = "#138808"
NAVY_BLUE = "#000080"

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Republic Day 2026")
screen.bgcolor("#050505") 
screen.tracer(0)

# Create drawing turtle
flag_turtle = turtle.Turtle()
flag_turtle.hideturtle()
text_turtle = turtle.Turtle()
text_turtle.hideturtle()

def draw_flagpole():
    flag_turtle.penup()
    flag_turtle.goto(-210, 200)
    flag_turtle.pendown()
    flag_turtle.color("grey")
    flag_turtle.begin_fill()
    for _ in range(2):
        flag_turtle.forward(12)
        flag_turtle.right(90)
        flag_turtle.forward(480)
        flag_turtle.right(90)
    flag_turtle.end_fill()

def draw_stripe(x_start, y_base, color, phase):
    """Draws a stripe with no borders and a smooth wave."""
    flag_turtle.penup()
    flag_turtle.color(color) # Set both pen and fill to the same color
    flag_turtle.fillcolor(color)
    flag_turtle.begin_fill()
    
    # Wave resolution (smaller step = smoother)
    step = 5
    
    # Top edge wave
    for x in range(0, 401, step):
        y = y_base + 12 * math.sin((x + phase) / 50.0)
        flag_turtle.goto(x_start + x, y)
        if x == 0: flag_turtle.pendown()
    
    # Right side
    curr_y = y_base + 12 * math.sin((400 + phase) / 50.0)
    flag_turtle.goto(x_start + 400, curr_y - 70)
    
    # Bottom edge wave
    for x in range(400, -1, -step):
        y = (y_base - 70) + 12 * math.sin((x + phase) / 50.0)
        flag_turtle.goto(x_start + x, y)
        
    flag_turtle.goto(x_start, y_base + 12 * math.sin(phase / 50.0))
    flag_turtle.end_fill()

def draw_ashoka_chakra(x_center, y_base, phase):
    """Draws the Chakra perfectly centered in the middle stripe."""
    # The middle stripe is 70 units tall. Midpoint is y_base - 35.
    # We must offset the Y by the wave function at the exact center point (x=200).
    center_offset = 200
    y_wave = (y_base - 35) + 12 * math.sin((center_offset + phase) / 50.0)
    
    flag_turtle.penup()
    flag_turtle.goto(x_center, y_wave - 28) # Adjust for circle radius
    flag_turtle.setheading(0)
    flag_turtle.color(NAVY_BLUE)
    flag_turtle.pensize(2)
    flag_turtle.pendown()
    flag_turtle.circle(28)
    
    # Spokes
    for i in range(24):
        flag_turtle.penup()
        flag_turtle.goto(x_center, y_wave)
        flag_turtle.setheading(i * 15)
        flag_turtle.pendown()
        flag_turtle.forward(28)
    flag_turtle.pensize(1)

def write_wishes():
    text_turtle.clear()
    text_turtle.penup()
    text_turtle.color("white")
    text_turtle.goto(0, -240)
    text_turtle.write("HAPPY REPUBLIC DAY", align="center", font=("Arial", 32, "bold"))
    text_turtle.goto(0, -280)
    text_turtle.color(SAFFRON)
    text_turtle.write("Honoring the Spirit of India - 2026", align="center", font=("Arial", 16, "italic"))

# --- Main Animation Loop ---
draw_flagpole()
phase = 0

try:
    while True:
        flag_turtle.clear()
        # Draw the stripes (x_start, y_base, color, phase)
        # We overlap them by 1 pixel to prevent 'breaking' lines
        draw_stripe(-198, 180, SAFFRON, phase)
        draw_stripe(-198, 110, WHITE, phase)
        draw_stripe(-198, 40, GREEN, phase)
        
        # Center the Chakra: start point (-198) + half width (200) = 2
        draw_ashoka_chakra(2, 110, phase)
        
        write_wishes()
        
        screen.update()
        phase += 6 
        time.sleep(0.01)
except turtle.Terminator:
    pass
