from turtle import Turtle, colormode, done

leo: Turtle = Turtle()

leo.penup()
leo.goto(0, 0)
leo.pendown()
colormode(255)
leo.color(10, 231, 229)

leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1

leo.fillcolor(32, 67, 93)
leo.end_fill()


bob: Turtle = Turtle()
bob.penup()
bob.goto(0, 0)
bob.pendown()
bob.color(1, 15, 15)
bob.speed(100)

side_length = 300
i: int = 0
while (i < 100):
    bob.forward(side_length)
    bob.left(121)
    i += 1
    side_length *= 0.97

done()