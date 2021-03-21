# Rainbow sky background

import turtle as t
t.speed(99999)

# Cloud element
def cloud(size, x, y):
    t.pensize(2)
    t.pencolor('white')
    t.fillcolor('white')
    t.goto(x, y)
    t.down()
    t.begin_fill()
    t.forward(size*50)
    t.circle(size*10,250)
    t.right(160)
    t.circle(size*15,190)
    t.right(160)
    t.circle(size*7.8,213)
    t.end_fill()
    t.up()
    t.home()

# The main function
def rainbow():

    # Sky color
    t.pencolor('#D9ECEF')
    t.fillcolor('#D9ECEF')
    t.begin_fill()
    t.forward(300)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(600)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(300)
    t.end_fill()
    t.up()

    # Clouds
    cloud(2, -200, 150)
    cloud(3, 120, 40)
    cloud(1, -250, 30)

    # Rainbow element
    t.forward(50)
    t.pencolor('purple')
    t.fillcolor('purple')
    t.left(90)
    t.down()
    t.begin_fill()
    t.circle(70, 180)
    t.right(90)
    t.forward(5)
    t.right(90)
    t.circle(-75,180)
    t.end_fill()
    t.right(180)
    t.pencolor('dark blue')
    t.fillcolor('dark blue')
    t.begin_fill()
    t.circle(75, 180)
    t.right(90)
    t.forward(5)
    t.right(90)
    t.circle(-80, 180)
    t.end_fill()
    t.right(180)
    t.begin_fill()
    t.pencolor('light blue')
    t.fillcolor('light blue')
    t.circle(80, 180)
    t.right(90)
    t.forward(5)
    t.right(90)
    t.circle(-85, 180)
    t.end_fill()
    t.right(180)
    t.begin_fill()
    t.pencolor('green')
    t.fillcolor('green')
    t.circle(85, 180)
    t.right(90)
    t.forward(5)
    t.right(90)
    t.circle(-90, 180)
    t.end_fill()

    t.right(180)
    t.begin_fill()
    t.pencolor('yellow')
    t.fillcolor('yellow')
    t.circle(90, 180)
    t.right(90)
    t.forward(5)
    t.right(90)
    t.circle(-95, 180)
    t.end_fill()

    t.right(180)
    t.begin_fill()
    t.pencolor('red')
    t.fillcolor('red')
    t.circle(95, 180)
    t.right(90)
    t.forward(5)
    t.right(90)
    t.circle(-100, 180)
    t.end_fill()

    t.up()
    t.home()

rainbow()
t.done()