import turtle
tim = turtle.Turtle()
def polygon(sides):
    totalAngles = (sides - 2)*180
    innerAngle = (totalAngles/sides)
    for i in range(sides):
        tim.forward(100)
        tim.right(180-innerAngle)

polygon(7)

turtle.done()