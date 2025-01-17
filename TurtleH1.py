import turtle

def draw_equilateral_triangle(side_length):
    for _ in range(3):
        turtle.forward(side_length)
        turtle.left(120)

turtle.penup()
turtle.goto(-500, 300)
turtle.pendown()

turtle.speed(1)
draw_equilateral_triangle(200)

turtle.penup()
turtle.goto(-250, 300)  
turtle.pendown()


turtle.left(90)
turtle.forward(200)
turtle.backward(100)
turtle.right(45)
turtle.forward(140)
turtle.backward(140)
turtle.right(90)
turtle.forward(140)


turtle.penup()
turtle.goto(0, 300)  
turtle.pendown()

turtle.done()
