import turtle as t


def tree(x: float, y: float) -> None:
    """Paint a beautiful tree."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    TRUNK_LENGTH = 100.0
    ANGLE = 90.0
    branch(TRUNK_LENGTH, ANGLE)
    t.update()


def branch(length: float, angle: float) -> None:
    t.setheading(angle)
    t.forward(length)

    if length < 3.0:
        ...
    else:
        branch(length * 0.75, angle + 25)
        branch(length * 0.7, angle - 23.0)
    t.setheading(angle + 100.0)
    t.forward(length)


t.tracer(0, 0)
t.speed(0)
tree(0.0, 0.0)
t.done()