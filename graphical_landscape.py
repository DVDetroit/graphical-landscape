'''

    Use turtle graphics and Python to create a graphical landscape. 

    1) The bottom half of the screen should be green.

    2) The top half of the screen should be blue.

    3) Draw grey mountains in the background using triangles.  Create at least 3 mountains of varying sizes.

    4) Draw an orange truck with black tires in the foreground.

    5) Draw your initials in the bottom right corner using forward(), right(), left(), penup() and pendown().  Do not use the write command.

    6) Include these instructions as comments at the beginning of your program.  Also comment each section, i.e. draw mountain, draw truck, etc.

    Attach your .py file to Blackboard.  Make sure you attach your .py file and not the .pyproj file.  If you attach the wrong file you will get zero credit.

    Don't forget the instructions as comments as well as code comments or you will loose points.
'''

import turtle
turtle.setup(640, 480)
turtle.speed(10)
#Creating the bottom half and painting it green

turtle.pencolor('green')
turtle.fillcolor('green')
turtle.begin_fill()
turtle.goto(300, 0)
turtle.goto(300, -220)
turtle.goto(-300, -220)
turtle.goto(-300, 0)
turtle.goto(0, 0)
turtle.end_fill()

#Moving the turtle via penup and go to start fresh and creating the sky and making it blue via the fill and pen color like we did with the terrain.
turtle.penup()
turtle.goto(300, 220)
turtle.pencolor('blue')
turtle.fillcolor('blue')
turtle.pendown()
turtle.begin_fill()
turtle.goto(300, 0)
turtle.goto(-300, 0)
turtle.goto(-300, 220)
turtle.goto(300, 220)
turtle.end_fill()


#Drawing the mountains and using fill in to make them grey.
turtle.penup()
turtle.goto(-210,0)
turtle.pencolor('grey')
turtle.fillcolor('grey')
turtle.pendown()
turtle.begin_fill()
#First mountain
turtle.forward(150)
turtle.left(120)
turtle.forward(150)
turtle.left(120)
turtle.forward(150)
turtle.left(120)

#Second mountain
turtle.forward(150)
turtle.forward(150)
turtle.left(120)
turtle.forward(150)
turtle.left(120)
turtle.forward(150)
turtle.left(120)

#Third mountain
turtle.forward(150)
turtle.forward(150)
turtle.left(120)
turtle.forward(150)
turtle.left(120)
turtle.forward(150)
turtle.left(120)
turtle.end_fill()


#Drawing the truck and painting it orange with black tires.
turtle.penup()
turtle.goto(-0, -0)  # Start position for the truck
turtle.pendown()
turtle.pencolor('orange')
turtle.fillcolor('orange')
turtle.begin_fill()
turtle.forward(50) #length of bed

#start of cab
turtle.left(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(40) #length of cab
turtle.right(90)
turtle.forward(60)

#truck + cab
turtle.right(90)
turtle.forward(90)
turtle.right(90)
turtle.forward(40)
turtle.end_fill()

# First tire
turtle.penup()
turtle.goto(25, -30)  # Position for first tire
turtle.pencolor('black')
turtle.fillcolor('black')
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)  # Radius of tire
turtle.end_fill()
turtle.penup()

# Second tire
turtle.goto(85, -30)  # Position for second tire
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()
turtle.penup()

#Drawing my initials

# Drawing K
turtle.penup()
turtle.goto(150, -100)
turtle.pendown()
turtle.setheading(90)
turtle.forward(50)
turtle.penup()
turtle.goto(150, -75)
turtle.pendown()
turtle.setheading(45)
turtle.forward(35)
turtle.penup()
turtle.goto(150, -75)
turtle.pendown()
turtle.setheading(-45)
turtle.forward(35)

# Drawing M
turtle.penup()
turtle.goto(190, -100)
turtle.pendown()
turtle.setheading(90)
turtle.forward(50)
turtle.goto(210, -100)
turtle.goto(230, -50)
turtle.setheading(270)
turtle.forward(50)


turtle.exitonclick()