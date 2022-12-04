from turtle import Screen,Turtle
import random

is_race_on=False
screen=Screen()
screen.setup(height=400,width=500)
user_bet=screen.textinput(title="make your bet",prompt="choose a color")
print(user_bet)
colors=["red","orange","yellow","green","blue","purple"]
y_posiitons=[-70,-40,-10,20,50,80]
all_turtles=[]

for turtle_index in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup
    new_turtle.goto(x=-230,y=-y_posiitons[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on=True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"you are won {winning_color}")
            else:
                print(f"you are lost ,winning color is {winning_color}")

        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)
         


screen.exitonclick()  