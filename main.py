import pandas as pd
from write import Writer
from turtle import Turtle, Screen
df = pd.read_csv("50_states.csv")

screen = Screen()
message = Turtle()
message.penup()
message.color("black")
screen.bgpic("blank_states_img.gif")
screen.setup(725, 600)
game_is_on = True
count = 0
while game_is_on:
    inp = screen.textinput(f"{count}/50 States", "Name")
    for i in df["state"]:
        if i == inp:
            count += 1
            wr = Writer(inp)
            break
    if count == 50:
        message.write("You won!!")
        game_is_on = False




screen.exitonclick()