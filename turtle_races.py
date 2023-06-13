from turtle import Turtle, Screen 
import random


SHELLS = {"light coral" : "red",
          "goldenrod" : "yellow", 
          "sandybrown" : "orange",
          "dark khaki" : "green", 
          "light steel blue" : "blue",
          "thistle" : "purple"}


# Window Setup 
wn = Screen()
wn.setup(500, 400)

all_turtles = []

# Creates and places racing turtles on screen
lane = 80
for shell in SHELLS:
    t = Turtle("turtle")
    t.color(shell)
    t.penup()
    t.setpos(-230, lane)
    all_turtles.append(t)
    lane -= 30  

# Stores user input in variable
bet = wn.textinput("Turtle Bets", "Which turtle will win? Select a colour.").lower().replace(" ", "")

start_race = False

if bet:
    start_race = True

while start_race:
    for t in all_turtles:
        if t.xcor() > 230:
            winner = t.pencolor() # Returns pen color of first turtle that reaches the end
            start_race = False 

            # Check is user bet won   
            if bet == SHELLS[winner]: 
                print(f"Congrats, the {bet} turtle won!")
            else:
                print(f"Aw, the {bet} turtle lost. Better luck next time.")
        
        # Moves each turtle by a unique distance 
        steps = random.randint(1, 10)
        t.forward(steps)
        
wn.exitonclick()