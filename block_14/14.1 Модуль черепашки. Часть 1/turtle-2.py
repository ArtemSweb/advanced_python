import turtle


turtle_1 = turtle.Turtle()
turtle_1.hideturtle()
turtle_1.fillcolor('brown')

turtle_1.begin_fill()

turtle_1.forward(100)
turtle_1.left(120)
turtle_1.forward(120)
turtle_1.left(120)
turtle_1.forward(120)
turtle_1.left(120)
turtle_1.forward(30)

turtle_1.end_fill()

turtle_2 = turtle.Turtle()
turtle_2.hideturtle()
turtle_2.fillcolor('green')

turtle_2.begin_fill()

for i in range(4):
    turtle_2.forward(80)
    turtle_2.right(90)

turtle_2.end_fill()