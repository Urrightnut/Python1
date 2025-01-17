import turtle

# Seadistame akna
window = turtle.Screen()
window.title("Sinilill Kevin")
window.bgcolor("white")

# Loo kilpkonn
flower = turtle.Turtle()

# Joonista vars
flower.color("green")
flower.pensize(10)
flower.penup()
flower.goto(0, -250)
flower.pendown()
flower.goto(0, -50)

# Joonista leht
flower.penup()
flower.goto(0, -100)
flower.pendown()
flower.begin_fill()
flower.color("green")
flower.goto(-50, -120)
flower.goto(0, -150)
flower.goto(0, -100)
flower.end_fill()

# Joonista sinine lill
flower.penup()
flower.goto(0, -50)
flower.pendown()
flower.color("blue")
flower.begin_fill()
flower.circle(50)
flower.end_fill()

# Tsentreeri hele sinine ring
flower.penup()
flower.goto(0, -30)
flower.pendown()
flower.color("light blue")
flower.begin_fill()
flower.circle(30)
flower.end_fill()

# Tsentreeri kollane ring
flower.penup()
flower.goto(0, -10)
flower.pendown()
flower.color("yellow")
flower.begin_fill()
flower.circle(10)
flower.end_fill()

# Lõpeta
flower.hideturtle()
window.mainloop()

