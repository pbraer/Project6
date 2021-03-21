# Land bottom

import turtle as t
t.speed(99999)

# Shadows element
def shadows(x, y):
    t.pensize(2)
    t.pencolor('#573E30')
    t.goto(x,y)
    t.down()
    t.circle(-10, 40)
    t.circle(15, 80)
    t.circle(-10,40)
    t.up()
    t.back(17)
    t.down()
    t.forward(5)
    t.up()
    t.home()

# The main function
def land():

    # Bottom color
    t.pencolor('#755441')
    t.fillcolor('#755441')
    t.begin_fill()
    t.forward(300)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(600)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(300)
    t.end_fill()
    t.up()
    shadows(-200, -30)
    shadows(-140, -110)
    shadows(-230,-160)
    shadows(-60, -50)
    shadows(0, -100)
    shadows(20, -180)
    shadows(100, -60)
    shadows(180, -90)

    t.up()
    t.home()

land()
t.done()
