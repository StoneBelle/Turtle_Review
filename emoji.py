from turtle import Turtle, Screen


# Star Formula
# 180 / num_points_on_star (i.e vertices)
# 180 - vertice_angle (i.e. exterior angle between 2 vertices) 

wn = Screen()
wn.screensize(800, 800)
 # Returns the coordinates of the clicked area on screen
def button_clicked(x, y):
    print(x, y) 


franklin = Turtle("turtle")
franklin.speed(5)

def make_face(x, y, colour):
    """Creates the face base of emoji"""
    franklin.penup()
    franklin.goto(x, y)
    franklin.pendown()

    franklin.color(colour)
    franklin.begin_fill()
    franklin.circle(120)
    franklin.end_fill()

def make_semi_circle(colour, my_dir, x, y, r, d):
    franklin.color(colour)
    franklin.penup()
    franklin.goto(x, y)
    franklin.pendown()
    franklin.seth(my_dir)
    franklin.begin_fill()
    franklin.circle(r, 180)
    franklin.lt(90)
    franklin.fd(r*d)
    franklin.end_fill()

def make_star(colour,x, y, num_vertex, size):
    franklin.penup()
    franklin.color(colour)
    franklin.goto(x, y)
    franklin.pendown()

    outer_angle = 180 - (180 / num_vertex)

    franklin.begin_fill()
    for v in range(num_vertex):
        franklin.fd(size)
        franklin.right(outer_angle)
    franklin.end_fill()



def emoji_one():
    """Starry Eyes Emoji"""
    make_face(-290, 141, "khaki")   # Face Base
    make_star("sandy brown",-370, 295, 5, 65)   # Left Eye
    make_star("sandy brown", -270, 295, 5, 65)  # Right Eye
    make_semi_circle("light coral", 270, -340, 225, 50, 2)   # Mouth    

    # Teeth
    franklin.color("white")
    franklin.begin_fill()
    franklin.seth(90)
    franklin.fd(10)
    franklin.rt(90)
    franklin.fd(100)
    franklin.rt(90)
    franklin.fd(10)
    franklin.end_fill()

    franklin.hideturtle()


def emoji_two():
    "Crying Emoji"
    make_face(-190, 141, "khaki")   # Face Base
    franklin.penup()
    franklin.goto(-98, 150)
    franklin.pensize(10)
    franklin.pendown()
    franklin.seth(90)
    franklin.pensize(10)
    franklin.color("black")
    franklin.circle(30, 175)

    franklin.penup()
    franklin.goto(17, 148)
    franklin.pendown()
    franklin.seth(90)
    franklin.circle(30, 175)
    franklin.pensize(5)
    make_semi_circle("light coral", 270, -119, 102, 50, 2)   # Mouth    


    # Tooth
    franklin.penup()
    franklin.goto(-54, 105)
    franklin.color("white")
    franklin.begin_fill()
    franklin.seth(270)
    franklin.fd(30)
    franklin.rt(90)
    franklin.fd(30)
    franklin.rt(90)
    franklin.fd(30)
    franklin.end_fill()

    franklin.hideturtle()


# Call emoji functions
emoji_one()
emoji_two()






wn.onscreenclick(button_clicked, 1)

wn.mainloop()
