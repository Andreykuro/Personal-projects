import turtle

win = turtle.Screen()
win.title("Moving Car")
win.bgcolor("white")

car = turtle.Turtle()
car.shape("square")
car.shapesize(2, 1)
car.color("black")
car.penup()


def move_forward():
    x, y = car.pos()
    car.setposition(x + 20, y)

def move_backward():
    x, y = car.pos()
    car.setposition(x - 20, y)

def move_left():
    x, y = car.pos()
    car.setposition(x, y - 20)

def move_right():
    x, y = car.pos()
    car.setposition(x, y + 20)

win.listen()
win.onkeypress(move_forward, "d")
win.onkeypress(move_backward, "a")
win.onkeypress(move_left, "s")
win.onkeypress(move_right, "w")

turtle.mainloop()
