import random, turtle

myscreen= turtle.Screen()

myscreen.bgcolor('light blue')
myscreen.setup(1.0,1.0)
myscreen.title('Physics Project Submitted to Sir.Vargas')

pen=turtle.Turtle()

pen.speed(0) 
pen.penup() 
pen.goto(-200,200) 
pen.pendown() 

for i in range(1,11): 
	pen.write(i,font=('Arial',10)) 
	pen.setheading(-90) 
	pen.forward(250) 
	if i==10: 
		pen.write(" FINISH",font=('Arial',14))
	pen.back(250)
	pen.penup() 
	pen.setheading(0) 
	pen.forward(50)  
	pen.down() 

finishLineX=250

def createTurtlePlayer(color, startx, starty): 
	player=turtle.Turtle()
	player.color(color) 
	player.shape("turtle") 
	player.penup() 
	player.goto(startx, starty) 
	player.pendown() 
	return player 

p1=createTurtlePlayer('red',-210,150) 
p2=createTurtlePlayer('blue',-210,100) 
p3=createTurtlePlayer('orange',-210,50)
p4=createTurtlePlayer('green',-210,0) 

while True:
	p1.forward(random.randint(5,10))
	if p1.pos()[0]>=finishLineX:
		p1.write(' I won the race!!',font=('Arial',30))
		break
	p2.forward(random.randint(5,10))
	if p2.pos()[0]>=finishLineX:
		p2.write(' I won the race!!',font=('Arial',30))
		break
	p3.forward(random.randint(5,10))
	if p3.pos()[0]>=finishLineX:
		p3.write(' I won the race!!',font=('Arial',30))
		break
	p4.forward(random.randint(5,10))
	if p4.pos()[0]>=finishLineX:
		p4.write(' I won the race!!',font=('Arial',30))
		break

turtle.done()
