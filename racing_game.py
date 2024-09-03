import turtle 
import random

screen = turtle.Screen()
screen.setup(800,800)

def move_next():
    francesco.forward(10)

turtle.listen()

francesco = turtle.Turtle()
francesco.shape("turtle")
francesco.color("blue")
francesco.shapesize(2,2)
francesco.penup()
francesco.goto(-380,100)

turtle.onkeypress(move_next, "Right")

steve = turtle.Turtle()
steve.shape("turtle")   
steve.color("red")
steve.shapesize(2,2)
steve.penup()
steve.goto(-380,0)

umair = turtle.Turtle()
umair.shape("turtle")
umair.color("green")
umair.shapesize(2,2)
umair.penup()
umair.goto(-380,-100)


boundary = turtle.Turtle()
boundary.shapesize(40,2)
boundary.color("black")
boundary.shape("square")
boundary.penup()
boundary.goto(380,0)

while True :
    step = random.randint(1,5)
    francesco.forward(step)

    step = random.randint(1,5)
    umair.forward(step)

    step = random.randint(1,5)
    steve.forward(step)


    if francesco.xcor() >= 350  or umair.xcor() >= 350 or steve.xcor() >= 350 :
        if francesco.xcor() >= umair.xcor() and francesco.xcor() >= steve.xcor() :
            turtle.write("francesco wins!", font = ("Arial", 40, "normal"))
            francesco.shapesize(4,4)
        elif umair.xcor() >= francesco.xcor() and umair.xcor() >= steve.xcor() :
            turtle.write("Umair wins", font = ("Arial", 40, "normal"))
            umair.shapesize(4,4)
        elif steve.xcor() >= francesco.xcor() and steve.xcor() >= umair.xcor() :
            turtle.write("Steve wins", font = ("Arial", 40, "normal"))
            steve.shapesize(4,4)
        break

turtle.mainloop()






