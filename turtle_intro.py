from turtle import Turtle, Screen
import prettytable
jimmy = Turtle()
my_screen = Screen()
jimmy.shape("turtle")
jimmy.color("navyblue")
jimmy.fillcolor("orange")

jimmy.begin_fill()
while True:
    jimmy.forward(200)
    jimmy.left(170)
    if abs(jimmy.pos())<1:
        break
jimmy.end_fill()

my_screen.exitonclick()
