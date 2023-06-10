from turtle import Turtle, Screen
import random 

# GOAL: Create a spirograph composed of different coloured circles, each with a radius of 100


SHELLS = ["indian red", "tan", "cornflower blue", "olive", "thistle"]



# Set up screen
wn = Screen()
wn.bgcolor("beige")

# Create a turtle object
t1 = Turtle()
t1.speed("fastest")
t1.hideturtle()
adjust = 10


while adjust != 360:
    t1.pencolor(random.choice(SHELLS))
    t1.circle(100)
    t1.setheading(adjust)
    adjust += 10

def make_spirograph():
    pass


wn.exitonclick()


