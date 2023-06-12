from turtle import Turtle, Screen
import random 

# GOAL: Create a spirograph composed of different coloured circles, each with a radius of 100


SHELLS = ["indian red", "tan", "cornflower blue", "olive", "thistle"]



# Screen Setup
wn = Screen()
wn.bgcolor("beige")

# Creates a turtle object
t1 = Turtle()
t1.speed("fastest")
t1.hideturtle()

def  make_spirograph(tilt, sides):
    for x in range(int(360/tilt)):
        t1.pencolor(random.choice(SHELLS))
        # Make a circle if sides == 1 or 2
        if sides == 1 or sides == 2:
            t1.circle(100)
        else:
            # Make a shape based on given sides
            for s in range(sides):
                t1.forward(100)
                t1.left(360/sides)

        # Shifts current pos by given tilt
        t1.setheading(t1.heading() + tilt)


make_spirograph(10, 2)
wn.exitonclick()


