import turtle
import time


def draw():
    colors = ['blue', 'red', 'green', 'yellow', 'orange', 'brown']

    turtle.pensize(5)
    turtle.bgcolor("black")
    turtle.speed(1000)

    for i in range(360):
        turtle.pencolor(colors[i % len(colors)])
        turtle.pensize(i / 50)
        turtle.forward(i)
        turtle.left(59)


    return


draw()


time.sleep(5)
