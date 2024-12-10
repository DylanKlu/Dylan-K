import turtle
t = turtle.Turtle()
t2 = turtle.Turtle()
t.hideturtle()
t2.hideturtle()
t.speed(0)
t2.speed(0)
screen = turtle.Screen()
screen.setup(500,500)



screen.bgcolor('red')
t2.penup()

t.write("Dylan Kluczkowski",font=("arial",30,"bold"),align="center")
t.penup()
t.goto(0,100)
t.pendown()

t.write("All About Me",font=("arial",30,"bold"),align="center")

t.penup()
t.goto(0,-100)
t.pendown()

t.write("Press enter for next page.",font=("arial",30,"bold"),align="center")



enter = input("press enter to begin")
t2.clear()
t.clear()
t2.penup()
screen.bgcolor('darkgreen')
turtle.addshape("food1.gif")
t2.shape("food1.gif")
t2.goto(0,-200)
a = t2.stamp()




t.penup()
turtle.addshape("food2.gif")
t2.shape("food2.gif")
t2.goto(-120,0)
c = t2.stamp()


t.penup()
turtle.addshape("food3.gif")
t2.shape("food3.gif")
t2.goto(-200,-200)
d = t2.stamp()


t.goto(0,10)


t.penup()
t.goto(0,100)
t.pendown()

t.write('1 is wings 2 is pizza 3 is chicken',font=("arial",20,"bold"),align="center")

t.penup()
t.goto(0,150)
t.pendown()
t.write("Press enter for next page.",font=("arial",20,"bold"),align="center")

t.penup()
t.goto(0,190)
t.pendown()

t.write("My Favorite Foods.",font=("arial",30,"bold"),align="center")


t.pencolor('black')
t.fillcolor("black")
t.penup()
t.goto(100,-85)
t.pendown()
t.begin_fill()
t.circle(80)
t.end_fill()
t.penup()
t.goto(0,50)
t.pendown()



enter = input("press enter to flip page")
t2.clear()
t.penup()
t.clear()

screen.bgcolor('light blue')


turtle.addshape("hobby1.gif")
t2.shape("hobby1.gif")
t2.goto(0,-200)
a = t2.stamp()




t.penup()
turtle.addshape("hobby2.gif")
t2.shape("hobby2.gif")
t2.goto(-120,0)
c = t2.stamp()


t.penup()
turtle.addshape("hobby3.gif")
t2.shape("hobby3.gif")
t2.goto(-200,-200)
d = t2.stamp()

t.penup()
turtle.addshape("hobby4.gif")
t2.shape("hobby4.gif")
t2.goto(150,-100)
d = t2.stamp()


t.goto(0,10)


t.penup()
t.goto(0,100)
t.pendown()

t.write('1 is football, 2 is playing madden, 3 is cooking, 4 is hunting',font=("arial",10,"bold"),align="center")
t.penup()
t.goto(0,150)
t.pendown()
t.write("Press enter for next page.",font=("arial",20,"bold"),align="center")
t.penup()
t.goto(0,190)
t.pendown()
t.write("My Favorite Hobbies.",font=("arial",30,"bold"),align="center")

t.pencolor('black')
t.fillcolor('pink')
t.begin_fill()
t.penup()
t.goto(-10, 10)
t.pendown()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.end_fill()

##############################################################

enter = input("press enter to flip page")
t2.clear()
t.penup()
t.clear()

screen.bgcolor('black')


turtle.addshape("movie1.gif")
t2.shape("movie1.gif")
t2.goto(100,0)
a = t2.stamp()




t.penup()
turtle.addshape("movie2.gif")
t2.shape("movie2.gif")
t2.goto(-100,0)
c = t2.stamp()


t.penup()
t.goto(0,100)
t.pendown()

t.pencolor('red')

t.write(' The Patriot ',font=("arial",30,"bold"),align="center")

t.penup()
t.goto(0,150)
t.pendown()
t.write("Press enter for next page.",font=("arial",30,"bold"),align="center")

t.penup()
t.goto(0,190)
t.pendown()
t.write("My Favorite Movie.",font=("arial",30,"bold"),align="center")


t.penup()
t.goto(0,-100)
t.pendown()

t.fillcolor("powderblue")
t.begin_fill()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(200)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.end_fill()




######################################################
enter = input("press enter to flip page")
t2.clear()
t.penup()
t.clear()

screen.bgcolor('mediumspringgreen')


turtle.addshape("sport.gif")
t2.shape("sport.gif")
t2.goto(100,0)
a = t2.stamp()




t.penup()
turtle.addshape("sport2.gif")
t2.shape("sport2.gif")
t2.goto(-100,0)
c = t2.stamp()


t.penup()
t.goto(0,100)
t.pendown()

t.pencolor('black')

t.write(' Boxing ',font=("arial",35,"bold"),align="center")

t.penup()
t.goto(0,-195)
t.pendown()
t.write("The end.",font=("arial",30,"bold"),align="center")
t.penup()
t.goto(0,195)
t.pendown()
t.write("My favorite Sport.",font=("arial",30,"bold"),align="center")

t.penup()
t.goto(0,150)
t.pendown()


t.penup()
t.goto(0,-100)
t.pendown()

t.fillcolor('purple')
t.begin_fill()
t.goto(50,-150)
t.goto(-50,-150)
t.goto(0,-100)
t.end_fill()



turtle.done()


















