import turtle

win = turtle.Screen()
win.title("Bouncing Ball")
win.bgcolor("white")

ball = turtle.Turtle()
ball.shape("circle")
ball.color("black")

ball.dx = 2
ball.dy = 2
ball.radius = 20


window_width = win.window_width()
window_height = win.window_height()

while True:
    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    
    if ball.xcor() + ball.radius > window_width/2 or ball.xcor() - ball.radius < -window_width/2:
        ball.dx = -ball.dx
    if ball.ycor() + ball.radius > window_height/2 or ball.ycor() - ball.radius < -window_height/2:
        ball.dy = -ball.dy

   
    win.update()
