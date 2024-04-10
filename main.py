import colorgram
import turtle as t
import random

colours = colorgram.extract("image.jpg", 30 )
rgb_colours = []

for colour in colours:
    r = colour.rgb.r
    g = colour.rgb.g
    b = colour.rgb.b

    new_colour = (r, g, b)

    rgb_colours.append(new_colour)

colour_list = [(197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216), (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177), (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28), (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199), (179, 17, 8), (233, 66, 34)]


tut = t.Turtle()
tut.penup()
t.colormode(255)
t.bgcolor("black")
tut.speed("fastest")
tut.setpos(-290, -240)
x = tut.xcor()
y = tut.ycor()
print(y)


for dots in range(20):

    for line in range(10):
        tut.color(random.choice(rgb_colours))
        tut.dot(10)
        tut.forward(50)
    y += 30
    tut.setpos(x, y)


screen = t.Screen()
screen.exitonclick()