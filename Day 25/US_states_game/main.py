import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")

image = './Day 25/US_states_game/blank_states_img.gif'
screen.addshape(image)
# turtle.shape(image)


data= pandas.read_csv("./Day 25/US_states_game/50_states.csv")
all_states = data.state.to_list()
# print(all_states)

guess_states =[]

while len(guess_states) < 50:
    
    answer_state = screen.textinput(title=f"{len(guess_states)}/50 correct states", prompt='what is another state name').title()
    print(answer_state)
   
    if answer_state =='Exit':
        # missing_states =[]
        # for state in all_states:
        #     if state not in guess_states:
        #         missing_states.append(state)

        # using list comprehension
        missing_states= [state for state in all_states if state not in guess_states]
        # print(missing_states)
        
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("./Day 25/US_states_game/missingStates.csv")
        break

    if answer_state in all_states:
        guess_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data= data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

# keep the screen on even after a click
# turtle.mainloop()
# screen.exitonclick()