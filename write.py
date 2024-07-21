from turtle import Turtle
import pandas as pd

fd = pd.read_csv("50_states.csv") # this is the csv file that contains the names of the states and their x and y coordinates



class Writer(Turtle):
    def __init__(self, state): #this is the constructor method
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.go_method(state) #calling the go_method to move the turtle to the correct position on the map
        self.write(state, True, "center")

    def go_method(self, state):
        fr = fd[fd.state == state] #getting the row where the state name matches the input
        corx = fr.x.item() #getting the x coordinate of the state
        cory = fr.y.item() #getting the y coordinate of the state
        self.goto(corx, cory) #moving the turtle to the correct position on the map

