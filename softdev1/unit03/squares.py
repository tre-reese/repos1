from operator import length_hint
import turtle
turtle.penup()
turtle.goto(-100,0)
turtle.fillcolor("blue")

def draw_square(length):
    turtle.begin_fill()
    turtle.pendown() 
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    print(length)
    
    turtle.end_fill()
    turtle.right(45)
    return length
def main():
    #draws first square
    draw_square(200)
    turtle.penup()
    turtle.goto(-100,-100)
    turtle.fillcolor("Red")
    #draws second square
    draw_square(140)
    turtle.penup()
    turtle.goto(-50,-150)
    turtle.fillcolor("purple")
    #draws 3rd square
    draw_square(98)
    turtle.goto(-0,-150)
    turtle.fillcolor("green")
    #draws 4th square
    draw_square(69)
    turtle.penup()
    turtle.fillcolor("yellow")
    turtle.goto(25,-125)
    #draws 5th square
    draw_square(49)
    turtle.goto(25,-100)
    turtle.fillcolor("white")
    #draws final square
    draw_square(34)
    
main()

input()