from turtle import Turtle
import pandas as pd

fd = pd.read_csv("50_states.csv")



class Writer(Turtle):
    def __init__(self, state):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.go_method(state)
        self.write(state, True, "center")

    def go_method(self, state):
        global corx, cory
        fr = fd[fd.state == state]
        for i in fr.x:
            corx = i
        for i in fr.y:
            cory = i

        self.goto(corx, cory)

