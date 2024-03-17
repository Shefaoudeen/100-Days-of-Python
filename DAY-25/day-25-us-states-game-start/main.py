import turtle
import pandas

states_data = pandas.read_csv("50_states.csv")
states = (states_data["state"].to_list())

state_turtles = []

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []

game_on = True

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct", prompt="What's another state's name: ").title()

    if answer_state == 'Exit':
        missing_state = [state for state in states if state not in guessed_states]
        '''
        missing_state = []
        for state in states:
            if state not in guessed_states:
                missing_state.append(state)
        '''
        print(missing_state)
        learn_states = pandas.DataFrame(missing_state)
        learn_states.to_csv("states_to_learn.csv")
        break

    if answer_state in states and answer_state not in guessed_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        actual_state = states_data[states_data.state == answer_state]
        t.goto(int(actual_state.x),int(actual_state.y))
        t.write(answer_state)
        guessed_states.append(answer_state)
    print(answer_state)




