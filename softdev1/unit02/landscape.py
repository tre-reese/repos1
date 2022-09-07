import turtle
def sq():
    turtle.forward(1000)
    turtle.right(-90)
    turtle.forward(1000)
    turtle.right(-90)
    turtle.forward(1000)
    turtle.right(-90)
    turtle.forward(1000)
    turtle.right(-90)
def sq2():
    turtle.forward(1000)
    turtle.right(-90)
    turtle.forward(230)
    turtle.right(-90)
    turtle.forward(1000)
    turtle.right(-90)
    turtle.forward(230)
    turtle.right(-90)
def sq3():
    turtle.forward(1000)
    turtle.right(-90)
    turtle.forward(100)
    turtle.right(-90)
    turtle.forward(1000)
    turtle.right(-90)
    turtle.forward(100)
    turtle.right(-90)
def sq4():
    turtle.forward(1000)
    turtle.right(90)
    turtle.forward(1000)
    turtle.right(90)
    turtle.forward(1000)
    turtle.right(90)
    turtle.forward(1000)
    turtle.right(90)
#background square functions^^d
def cloud():
    turtle.color("white")
    turtle.begin_fill()
    turtle.circle()
    radius =50
    turtle.end_fill()
#cloud func
def circle():
    turtle.circle(50)
turtle.goto(-500,0)
def main():
#sky
    turtle.fillcolor("navy")
    turtle.pencolor("navy")
    turtle.begin_fill()
    sq()
    turtle.end_fill()
    turtle.penup
    turtle.goto(-500,0)
    turtle.pendown
    turtle.pencolor("darkblue")
    turtle.fillcolor("darkblue")
    turtle.begin_fill()
    sq2()
    turtle.end_fill()
    turtle.penup
    turtle.goto(-500,0)
    turtle.pendown
    turtle.pencolor("mediumblue")
    turtle.fillcolor("mediumblue")
    turtle.begin_fill()
    sq3()
    turtle.end_fill()
    turtle.penup
    #sun
    turtle.goto(100,-100)
    turtle.fillcolor("orange")
    turtle.begin_fill()
    turtle.pencolor("yellow")
    turtle.circle(120)
    turtle.end_fill()
    turtle.penup
    #grass
    turtle.pencolor("darkgreen")
    turtle.goto(-500,0)
    turtle.fillcolor("darkgreen")
    turtle.begin_fill()
    sq4()
    #road
    turtle.end_fill()
    turtle.pencolor("black")
    turtle.goto(0,0)
    turtle.pendown
    turtle.goto(-300,-400)
    turtle.fillcolor("grey")
    turtle.begin_fill()
    turtle.forward(600)
    turtle.right(-90)
    turtle.goto(50,0)
    turtle.goto(0,0)
    turtle.end_fill()
    turtle.penup
    #mountains
    turtle.goto(-300,0)
    turtle.fillcolor("brown")
    turtle.pencolor("brown")
    turtle.begin_fill()
    turtle.pendown
    turtle.goto(-250,200)
    turtle.goto(-200,0)
    turtle.goto(-300,0)
    turtle.goto(-200,0)
    turtle.goto(-150,135)
    turtle.goto(-100,0)
    turtle.goto(-200,0)
    turtle.goto(-255,0)
    turtle.goto(-200,150)
    turtle.goto(-155,0)
    turtle.end_fill()
    turtle.penup()
   
#shrub
    turtle.goto(-275,-200)
    turtle.pendown()
    turtle.color("green")
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.circle(70)
    turtle.penup()
    turtle.goto(-300,-200)
    turtle.pd()
    turtle.circle(70)
    turtle.pu()
    turtle.goto(-280,-180)
    turtle.pd()
    turtle.circle(70)
    turtle.end_fill()
   
main()
input()