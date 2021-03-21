# Cloudy sky background

import turtle as t
t.speed(99999)

# Cloud element
def cloud(size, x, y):
    t.pensize(2)
    t.pencolor('#88898F')
    t.fillcolor('#B8BAC1')
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
def clouds():

    # Sky color
    t.pencolor('#7396BF')
    t.fillcolor('#7396BF')
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
    cloud(3, 50, 50)
    cloud(1, -100, 20)
    cloud(2, -200, 90)

    t.up()
    t.home()

clouds()
t.done()
