"""
Draws a sky filled with stars and planets.

@author
"""

import random
from sys import builtin_module_names
import turtle

def tweak(speed, tracer):
    """
    Adjust the turtle's speed and tracer settings so that it can be sped up
    or slowed down as needed for visual debugging.
    """
    turtle.speed(speed)
    turtle.tracer(tracer)

def random_yellow():
    """
    Sets the turtle's fill color to a random shade of yellow using RGB values.
    """
    # the random.random() function returns a floating point value between
    # 0.1 and 1.0. This expression guarantees that the red value will be
    # between 0.5 and 1.0.
    red = 0.5 + random.random() * 0.5
    green = red
    blue = red / 2

    # the turtle color can be set using RGB values ranging from 0.0 to 1.0. In
    #  this case the red and green values are between 0.5 and 1.0 and the blue
    # value is half the value - this guarantees a shade of yellow.
    turtle.color(red, green, blue)
    turtle.fillcolor(red, blue, green)


def random_move():
    """
    Moves the turtle to a random location and orientation on the screen.
    """
    x = random.randint(-350, 350)
    #syntax error, missing "," after 1000, to solve i looked at the line above
    y = random.randint(-350, 350)
    turtle.goto(x, y) 

    angle = random.randint(0, 360)
# sytax error, missing ":", functions need both "()" and ":"
def draw_star(length):
    """
    Draws a star at the turtle's current location and orientation.
    """
    random_yellow()

    turtle.down()
    turtle.fillcolor("yellow")
    turtle.begin_fill()

    turtle.forward(length)
    turtle.left(36)
    turtle.forward(length)
    turtle.right(108)

    turtle.forward(length)
    turtle.left(36)
    turtle.forward(length)
    turtle.right(108)

    turtle.forward(length)
    turtle.left(36)
    turtle.forward(length)
    turtle.right(108)

    turtle.forward(length)
    turtle.left(36)
    turtle.forward(length)
    turtle.right(108)

    turtle.forward(length)
    turtle.left(36)
    turtle.forward(length)
    turtle.right(108)

    turtle.end_fill()    
#Draws 10 stars per call
def stars():
    length = 30
    turtle.penup()
    turtle.goto(200,0)
    turtle.pendown()
    draw_star(length)
    turtle.left(30)
    turtle.penup()
    random_move()
    turtle.pendown()
    draw_star(length)
    turtle.penup()
    random_move()
    turtle.pendown()
    draw_star(length)
    turtle.penup()
    random_move()
    turtle.pendown()
    draw_star(length)
    turtle.penup()
    random_move()
    turtle.pendown()
    draw_star(length)
    turtle.penup()
    random_move()
    turtle.pendown()
    draw_star(length)
    turtle.penup()
    random_move()
    turtle.penup()
    random_move()
    turtle.pendown()
    draw_star(length)
    turtle.pendown()
    draw_star(length)
    turtle.penup()
    random_move()
    turtle.pendown()
    draw_star(length)
    turtle.penup()
    random_move()
    turtle.pendown()
    draw_star(length)
#draws a planet
def planets():
    radius = int(input("enter a rad: "))
    turtle.fillcolor("purple")
    turtle.circle(radius)
    turtle.penup()
    random_move()
    turtle.pendown()
def draw_celestial_bodies():
    stars()
    planets()
    stars()
    stars()
    planets()
    stars()
    stars()
    planets()
    stars()
    stars()
    stars()
    stars()
    stars()
def main():
    """
    Should ultimately draw a night sky filled with stars and planets.
    """
    turtle.bgcolor("black")
    tweak(True, 1)
    length = int(input("Enter length of star to draw (e.g. 100): "))
    draw_star(length)
    tweak(True, 1)
    draw_celestial_bodies()
    turtle.up()
    input("Press enter to continue...")

main()