import turtle
import random

MAX_X = 400 # the maximum x value in both directions
MAX_Y = 500 # the maximum y value in both directions

def random_color():
    """
    Returns a randomly selected color string.
    """
    color = random.randint(1, 10)
    if color == 1:
        return "red"
    if color == 2:
        return "orange"
    if color == 3:
        return "yellow"
    if color == 4:
        return "green"
    if color == 5:
        return "blue"
    if color == 6:
        return "purple"
    if color == 7:
        return "pink"
    if color == 8:
        return "skyblue"
    if color == 9:
        return "brown"
    if color == 10:
        return "magenta"


def draw_ball():
    radius = 59
    turtle.fillcolor("Red")
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

    turtle.fillcolor("white")
    turtle.color("white")
    turtle.begin_fill()
    turtle.circle(17.7)
    turtle.end_fill()
draw_ball()
input()