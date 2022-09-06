
import turtle
import pandas

screen = turtle.Screen()
screen.title("us states game")
picture = "blank_states_img.gif"
screen.addshape(picture)
turtle.shape(picture)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
gussed_state = []
while len(gussed_state) <50:
    answerd_state = screen.textinput(title=f"{len(gussed_state)}/50 states correct ",prompt="Whats another states name?").title()
    print(all_states)
    if answerd_state == "Exit":
        missing_state = []
        for state in all_states:
            if state not in gussed_state:
                missing_state.append(state)
        new_state = pandas.DataFrame(missing_state)
        print(new_state.to_csv("missed_state.csv"))
        break

    if answerd_state in all_states:
        gussed_state.append(answerd_state)
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        coordination = data[data.state == answerd_state]
        tim.goto(int(coordination.x),int(coordination.y))
        tim.write(answerd_state)





screen.exitonclick()