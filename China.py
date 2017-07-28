import turtle
def main():
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    rect(t)
    stars(t)
    turtle.done()
def rect(t):
    t.color("red","red")
    t.up()
    t.goto(-300, -200)
    t.down()
    t.begin_fill()
    t.goto(-300, 200)
    t.goto(300, 200)
    t.goto(300, -200)
    t.goto(-300, -200)
    t.end_fill()
def STAR(t):
    t.pencolor("yellow")
    t.fillcolor("yellow")
    t.down()
    t.begin_fill()
    for i in range(5):
        t.forward(90)
        t.right(144)
    t.end_fill()
    t.up()
def star(t):
    t.pencolor("yellow")
    t.fillcolor("yellow")
    t.down()
    t.begin_fill()
    for i in range(5):
        t.forward(30)
        t.right(144)
    t.end_fill()
    t.up()
def stars(t):
    x=-260
    y=125
    t.up()
    t.goto(x,y)
    STAR(t)
    t.left(66)
    m=150
    n=120
    for i in range(4):
        t.right(22)
        if i == 0 or i ==3:
            t.goto(-150,m)
            star(t)
            m=60
        else:
            t.goto(-140,n)
            star(t)
            n=90
main()