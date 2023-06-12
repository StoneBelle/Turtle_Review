from turtle import Turtle, Screen


# GOAL: Create an Etch-a-Sketch that can go forward & backward, but also diagonal

# Window & Pointer setup
pointer = Turtle()
wn = Screen()

def forward():
    pointer.fd(10)

def backward():
    pointer.bk(10)

def left():
    new_heading = pointer.heading() + 20
    pointer.seth(new_heading)

def right():
    new_heading = pointer.heading() - 20
    pointer.seth(new_heading)

def clear():
    pointer.reset()
 


wn.listen()  # Activates event listner 
# Events are typical things a user can do on a screen 
# e.g. press keys or click with mouse


# Bind function to keys 1 
wn.onkey(forward, "w")
wn.onkey(backward, "s")
wn.onkey(left, "a")
wn.onkey(right, "d")
wn.onkey(clear, "c")


wn.exitonclick()





















































































































  
