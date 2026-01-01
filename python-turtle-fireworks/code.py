import turtle
import random
import math
import time

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("New Year Firework Streaks")
screen.tracer(0)

text_pen = turtle.Turtle()
text_pen.hideturtle()
text_pen.penup()

def update_text():
    colors = ["#FFD700", "#FF3366", "#00FFCC", "#FFFFFF", "#ADFF2F"]
    text_pen.clear()
    text_pen.goto(0, -20)
    text_pen.color(random.choice(colors))
    text_pen.write("HAPPY NEW YEAR!", align="center", font=("Verdana", 50, "bold"))

def create_particle(x, y, color):
    p = turtle.Turtle()
    p.shape("circle")
    p.shapesize(0.05) 
    p.color(color)
    p.width(2)        
    p.penup()
    p.goto(x, y)
    p.pendown()       
    
    angle = random.uniform(0, 2 * math.pi)
    speed = random.uniform(4, 12)
    p.dx = math.cos(angle) * speed
    p.dy = math.sin(angle) * speed
    return p

def run_celebration():
    target_x = random.randint(-250, 250)
    target_y = random.randint(50, 250)
    
    rocket = turtle.Turtle()
    rocket.shape("circle")
    rocket.shapesize(0.1)
    rocket.color("gray")
    rocket.width(1)
    rocket.penup()
    
    start_x = random.randint(-350, 350)
    rocket.goto(start_x, -300)
    rocket.pendown() 
    
    steps = 15
    for i in range(steps):
        rocket.goto(
            rocket.xcor() + (target_x - start_x) / steps,
            rocket.ycor() + (target_y - (-300)) / steps
        )
        screen.update()
    
    rocket.clear() 
    rocket.hideturtle()
    
    update_text()

    particles = []
    explosion_color = random.choice(["#FF5733", "#FFD700", "#00FFFF", "#FF00FF", "#FFFFFF"])
    
    for _ in range(40): 
        particles.append(create_particle(target_x, target_y, explosion_color))
    
    for _ in range(35):
        for p in particles:
            p.dy -= 0.3
            p.goto(p.xcor() + p.dx, p.ycor() + p.dy) # Draw the next segment of path
            p.dx *= 0.92
            p.dy *= 0.92
        screen.update()
    
    for p in particles:
        p.clear()
        p.hideturtle()

update_text()

try:
    while True:
        run_celebration()
except turtle.Terminator:
    pass
