import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

guessed_states = []
correct_states = 0
all_states = data.state.to_list()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{correct_states}/50 States Correct",
                                    prompt="What's another State's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        if answer_state not in guessed_states:
            answer_data = data[data.state == answer_state]

            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(int(answer_data.x), int(answer_data.y))
            t.write(answer_state)

            correct_states += 1
            guessed_states.append(answer_state)
