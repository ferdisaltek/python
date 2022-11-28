from turtle import Turtle ,Screen
# color ('red','yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos())<1:
#         break
# end_fill()
# done()

# the_turtle=Turtle()
# the_turtle.shape("turtle")
# the_turtle.color("red")
# # the_turtle.forward(200)
# # the_turtle.right(90)
# the_turtle.forward(200)
# the_turtle.right(90)
# the_turtle.forward(200)
# the_turtle.right(90)
# the_turtle.forward(200)

# for i in range(4):
#     the_turtle.forward(200)
#     the_turtle.right(90)


# for i in range(15):
#     the_turtle.forward(10)
#     the_turtle.penup()
#     the_turtle.forward(10)
#     the_turtle.pendown



import turtle as t
import random

tim = t.Turtle()

########### Challenge 3 - Draw Shapes ########

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 10):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)