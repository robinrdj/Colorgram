###This code will not work in repl.it as there is no access to the colorgram package here.###

import colorgram
import random
import turtle
from turtle import Turtle, Screen

# import turtle as t(alias name)

# creating turtle object
turtle.colormode(255)
timmy = Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
timmy.shape("turtle")
timmy.color("red")

# creating screen object
screen = Screen()

# using colorgram to extract colors
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)

# putting extracted colors in a list
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
print(rgb_colors)

# setting turtle to the initial position
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
no_of_dots  = 100

# dotting colors on the screen
for dotcount in range(1,no_of_dots+1):
    timmy.dot(20, random.choice(extracted_colors))
    timmy.forward(50)

    if dotcount%10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)
screen.exitonclick()