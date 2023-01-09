"""Draw a house."""
__author__ = "730529618"

from turtle import Turtle, colormode, done 

leo: Turtle = Turtle()


def main() -> None:
    """The entrypoint of my scene."""
    leo: Turtle = Turtle()
    draw_rectangle(leo, -230, -100, 170, 150)
    colormode(255)
    leo.color(84, 59, 33)
    leo.begin_fill()  
    draw_triangle(leo, -270, 50, 250)
    leo.end_fill()
    window(leo, -200, 0, 25)
    window(leo, -160, 0, 25)
    window(leo, -120, 0, 25)
    sun(leo, 130, 180, 25)

    done()


def draw_rectangle(leo: Turtle, x: float, y: float, w: float, length: float) -> None:
    """Draw the base for the flag."""
    leo.penup()
    leo.goto(x, y) 
    leo.setheading(0.0)
    leo.pendown()
    leo.forward(w)
    leo.left(90)
    leo.forward(length)
    leo.left(90)
    leo.forward(w)
    leo.left(90)
    leo.forward(length)
    leo.left(90)


def draw_triangle(leo: Turtle, x: float, y: float, length: float) -> None:
    """Draw a triangle."""
    leo.penup()
    leo.goto(x, y) 
    leo.setheading(0.0)
    leo.pendown()
    i: int = 0
    while (i < 3):
        leo.forward(length)
        leo.left(120)
        i = i + 1


def window(leo: Turtle, x: float, y: float, length: float) -> None:
    """Draw a window."""
    leo.penup()
    leo.goto(x, y) 
    leo.setheading(0.0)
    leo.pendown()
    i = 0
    while i < 4:
        leo.forward(length)
        leo.left(90)
        i += 1
    leo.penup()
    leo.goto(x, y + length / 2)
    leo.pendown()
    leo.forward(length)
    leo.penup()
    leo.goto(x + length / 2, y)
    leo.pendown()
    leo.left(90)
    leo.forward(length)


def sun(leo: Turtle, x: float, y: float, radius: float) -> None:
    """Draw a sun."""
    leo.penup()
    leo.goto(x, y)
    leo.pendown()
    leo.color("black", "red")
    leo.begin_fill()
    leo.circle(radius)
    leo.end_fill()


if __name__ == "__main__":
    main()