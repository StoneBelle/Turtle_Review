from turtle import Turtle, Screen
import random 


SHELLS = ["indian red", "cornflowerblue", "olive", "deep pink"]

# Create a turtle object 
# t1 = Turtle()
# t1.shape("turtle")
# t1.color("olive")

# Set up my screen 
screen = Screen()


# Create a dashed line 
def make_dashes(t):
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()


# Create a sqaure
def make_square(t):
    for x in range(4):
        t.backward(200)
        t.right(90)


# Function to create any shape
def make_shape(sides, size):
    
    # Create & setup a turtle instance
    i = Turtle()
    i.hideturtle()
    i.color(random.choice(SHELLS))
    
    # Determine the angle of shape 
    angle = 360/round(sides)
    for s in range(round(sides)):
        i.forward(size)
        i.left(angle)


for shape in range(3, 11):
    make_shape(shape, 100)



    




# make_square(t1)



screen.exitonclick()

