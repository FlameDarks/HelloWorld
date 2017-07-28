import turtle
def main():
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    juxing(t)
    redwhite(t)
    bluejx(t)
    stars(t)
    turtle.done()
def juxing(t):
    t.pencolor("red")
    t.up()
    t.goto(-494, -260)
    t.down()
    t.goto(-494, 260)
    t.goto(494, 260)
    t.goto(494, -260)
    t.goto(-494, -260)
def redwhite(t,n=0):
    t.pencolor("red")
    t.fillcolor("red")
    for i in range(13):
        n += 40
        t.up()
        t.goto(-494, -260 + n)
        if i % 2 == 0:
            t.begin_fill()
            t.down()
            for i in range(2):
                t.forward(988)
                t.right(90)
                t.forward(40)
                t.right(90)
            t.end_fill()
        else:
            t.down()
            t.forward(988)
def bluejx(t):
    t.pencolor("blue")
    t.fillcolor("blue")
    t.up()
    t.goto(-494,-20)
    t.down()
    t.begin_fill()
    for i in range(2):
        t.forward(396)
        t.left(90)
        t.forward(280)
        t.left(90)
    t.end_fill()
def star(t):
    t.pencolor("yellow")
    t.fillcolor("yellow")
    t.down()
    t.begin_fill()
    for i in range(5):
        t.forward(15)
        t.right(144)
    t.end_fill()
    t.up()
def stars(t):
    x=-484
    y=250
    t.up()
    t.goto(x,y)
    for i in range(11):
        if i % 2 == 0:
            for a in range(5):
                y-=60
                star(t)
                t.goto(x,y)
        else:
            y-=30
            t.goto(x,y)
            for a in range(4):
                y -= 60
                star(t)
                t.goto(x,y)
        x += 35
        y = 250
        t.goto(x,y)
main()