from turtle import Turtle, Screen
import random


PALETTE = ["light coral", "sandy brown", "goldenrod", "thistle", "light steel blue"]


def make_shape(pos, sides, task, tilt):
    # Creates a turtle instance 
    franklin = Turtle()
    franklin.hideturtle()
    franklin.penup()
    franklin.goto(pos)
    franklin.pendown()
    franklin.speed(0)

    # Selects random colour for pen outline and pen fill
    franklin.color(random.choice(PALETTE), random.choice(PALETTE))
    
    # Creates a spirograph based on given amount of sides
    if task == "spiro":
        spin = int(360/tilt) # Determines amount of rotations

        for x in range(spin):
            if sides == 1 or sides == 2:
                franklin.circle(20)
            else:
                for s in range(sides):
                    franklin.fd(50)
                    franklin.right(360/sides)
            
            # Update turtle heading (i.e. direction)
            new_hd = franklin.heading() + tilt
            franklin.seth(new_hd)

    # Creates a stars based on given amount of points
    elif task == "star":
        # Star angle formula
        # 180 / num_points_on_star (i.e the point angle)
        # 180 - point_angle (i.e. gap between the point) 
        
        angle = 180 - (180 / tilt)

        franklin.begin_fill()
        for x in range(tilt): # tilt represents num of points on star
            franklin.forward(150) 
            franklin.left(angle) # angle represesnts the angle between the points
        franklin.end_fill()

    # Creates a shape based on given sides
    else:
        franklin.begin_fill()
        if sides == 1 or sides == 2:
            franklin.circle(30)
        else:    
            for x in range(sides):    
                franklin.fd(60)
                franklin.rt(360/sides) # Turns turtle right by given degree
        franklin.end_fill()

# Window Set Up 
wn = Screen()
wn.setup(600, 600)


make_shape((-230, 230), 1, "shape", 0)
make_shape((-210, 200), 3, "shape", 0)
make_shape((-150, 140), 4, "shape", 0)
make_shape((-220, 50), 5, "shape", 0)
make_shape((-220, -60), 6, "shape", 0)
make_shape((125,-120), 7, "spiro", 10)
make_shape((75, 130), 7, "star", 15)
make_shape((-100, -10), 7, "star", 5)


wn.mainloop()