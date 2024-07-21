import pandas as pd
from write import Writer
from turtle import Turtle, Screen
df = pd.read_csv("50_states.csv")   #this is the csv file that contains the names of the states and their x and y coordinates
screen = Screen()  #creating a screen object
message = Turtle() #creating a turtle object to write the message
message.hideturtle()
message.penup()
message.color("black")
screen.bgpic("blank_states_img.gif") #setting the background image to the map of the US
screen.setup(725, 600)
game_is_on = True
count = 0
states = df.state.to_list() #converting the state column of the dataframe to a list
while game_is_on:
    inp = screen.textinput(f"{count}/50 States", "Name").title() #taking the input from the user
    if inp == "Quit": #if the user types quit, the game will end
        game_is_on = False
        new_df = pd.DataFrame(states) #creating a new dataframe from the list of states that were missed
        new_df.to_csv("missed_states.csv") #writing the missed states to a csv file

    else:
        for i in df["state"]: #iterating through the states
            if i == inp: #if the input matches a state
                count += 1 #increment the count by 1
                wr = Writer(inp) #create a writer object and write the state name on the map
                states.remove(inp) #remove the state from the list of states
                break
    if count == 50:
        message.write("You won!!") #if the count reaches 50, the user has won the game
        game_is_on = False



screen.exitonclick()
