# Road bottom

import turtle as t
t.speed(99999)

# Brick element
def brick():
    t.down()
    t.pensize(3)
    t.pencolor('#B38062')
    t.fillcolor('#B35E19')
    t.begin_fill()
    t.forward(50)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(50)
    t.end_fill()
    t.up()

# A half of brick element
def half_brick():
    t.down()
    t.pensize(3)
    t.pencolor('#B38062')
    t.fillcolor('#B35E19')
    t.begin_fill()
    t.forward(25)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(25)
    t.end_fill()
    t.down()

# The main function
def road():
    t.pensize(3)
    t.pencolor('white')
    t.fillcolor('#B35E19')
    t.up()
    t.goto(-300, 0)
    for s in range(1,5):
        for i in range(1,13):
            brick()
        t.up()
        t.back(600)
        t.right(90)
        t.forward(25)
        t.left(90)
        t.down()
        half_brick()
        for j in range(1,12):
            brick()
        half_brick()
        t.up()
        t.back(600)
        t.right(90)
        t.forward(25)
        t.left(90)

    t.up()
    t.home()

road()
t.done()
