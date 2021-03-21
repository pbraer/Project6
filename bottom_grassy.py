# Grassy bottom

import turtle as t
t.speed(99999)

# Grass element
def grass(size, x, y):
    t.pensize(2)
    t.pencolor('#205205')
    t.goto(x,y)
    t.down()
    t.left(70)
    t.forward(size*18)
    t.left(160)
    t.forward(size*20)
    t.right(130)
    t.forward(size*10)
    t.left(150)
    t.forward(size*10)
    t.right(140)
    t.forward(size*20)
    t.left(160)
    t.forward(size*20)
    t.right(140)
    t.forward(size*10)
    t.left(160)
    t.forward(size*10)
    t.up()
    t.home()

# The main function
def grassy():

    # Bottom color
    t.pencolor('#2B6E07')
    t.fillcolor('#2B6E07')
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

    # Grass
    t.speed(199999)
    grass(1, -250, - 30)
    grass(2, -200, -150)
    grass(0.7, -160, -70)
    grass(1.5, -85, -90)
    grass(0.8, 0, -35)
    grass(1.3, 20, -140)
    grass(1.15, 70, -70)
    grass(2, 200, -170)
    grass(1, 270, -40)
    grass(0.7, 200, -100)

    t.up()
    t.home()

grassy()
t.done()
