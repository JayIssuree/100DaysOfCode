from operator import index
import turtle
import pandas

data = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
writer = turtle.Turtle()
writer.pu()
writer.ht()

correct_states = 0
prev_answers = {}

def check_answer(answer):
    if answer not in prev_answers and (data.state == answer).any():
        prev_answers[answer] = True
        write_answer(answer)
        global correct_states
        correct_states += 1

def write_answer(answer):
    coordinates = data[data.state == answer]
    x = int(coordinates.x)
    y = int(coordinates.y)
    writer.goto(x, y)
    writer.write(answer)

def states_to_learn():
    global prev_answers
    prev_answers = list(prev_answers.keys())
    to_learn = data[~data.state.isin(prev_answers)].state
    to_learn.to_csv("states_to_learn.csv", index=False)
        


while correct_states != 50:
    answer_state = screen.textinput(title=f"{correct_states}/50 States Correct", prompt="Enter a State Name").title()
    if answer_state == "Exit":
        states_to_learn()
        break
    check_answer(answer_state)