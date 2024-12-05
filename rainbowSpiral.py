import turtle
turtle.Screen().bgcolor("black")
sc=turtle.Screen()
sc.setup(400,300)

board=turtle.Turtle()
board.speed(1)
board.color("yellow")
turtle.title("square")

sidelength=100
angle=30
gap=5
num_squares=30
board.penup()
board.pendown()

for _ in range(num_squares):
    board.forward(sidelength)
    board.left(90)
    board.forward(sidelength)
    board.left(90)
    board.forward(sidelength)
    board.left(90)
    board.forward(sidelength)

for _ in range(4):
    board.forward(sidelength)
    board.left(90)
    board.left(angle)
    sidelength += gap
    