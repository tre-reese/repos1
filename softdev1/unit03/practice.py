

import turtle
def main():
    turtle.penup()
    turtle.goto(-400,-300)
    turtle.pencolor("blue")
    turtle.fillcolor("blue")
    turtle.begin_fill()
    turtle.pendown()
    turtle.goto(400,-300)
    turtle.goto(400,400)
    turtle.goto(-400,400)
    turtle.goto(-400,-300)
    turtle.end_fill()
    turtle.penup()
    def snow_man():
        turtle.fillcolor("white")
        turtle.pencolor("black")
        turtle.goto(0,0)
        turtle.begin_fill()
        turtle.pendown()
        turtle.circle(50)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(0,100)
        turtle.begin_fill()
        turtle.pendown()
        turtle.circle(50*.75)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(0,175)
        turtle.begin_fill()
        turtle.pendown()
        turtle.circle(50*.56)
        turtle.end_fill()
    snow_man()
main()
input()