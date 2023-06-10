from turtle import Turtle, Screen
import random


# GOALS: 
# Move the turtle 10px in a random direction
# Esure the pen line is visible and in a random colour


SHELLS = ["indian red", "tan", "cornflower blue", "olive", "thistle"]

NAV = [0, 90, 180, 270]

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)
# Create the turtle 
franklin = Turtle()
franklin.hideturtle()
franklin.speed(0)
franklin.pensize(10) # Adjusts the pen thickness




wn = Screen()
wn.screensize(500, 400) # Adjusts screensize, W x H
wn.colormode(255) # 



for x in range(300):
    franklin.pencolor(random.choice(SHELLS))
    franklin.pencolor(random_colour())
    franklin.setheading(random.choice(NAV))
    franklin.forward(20)









wn.exitonclick()
