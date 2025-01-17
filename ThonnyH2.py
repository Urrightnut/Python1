import turtle

window = turtle.Screen()
window.title("Olümpiarõngad Kevin")
window.setup(width=500, height=400)

def draw_circle(color, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.pensize(6)
    turtle.circle(50)

turtle.speed(0)

draw_circle("blue", -120, 0)
draw_circle("black", 0, 0)
draw_circle("red", 120, 0)
draw_circle("yellow", -60, -50)
draw_circle("green", 60, -50)

turtle.hideturtle()
turtle.done()