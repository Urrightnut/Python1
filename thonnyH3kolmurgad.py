import turtle

# Loome muutujad
kylje_pikkus = 100
nurk = 120
kujundi_varv = "red"

# Loome kilpkonna
pen = turtle.Turtle()
pen.color(kujundi_varv)

# Funktsioon kolmnurga joonistamiseks
def joonista_kolmnurk(pikkus):
    for _ in range(3):
        pen.forward(pikkus)
        pen.left(nurk)

# Alguspunkti seadistamine
pen.penup()
pen.goto(-kylje_pikkus * 1.5, 0)
pen.pendown()

# Joonista 3 kolmnurka
for i in range(3):
    joonista_kolmnurk(kylje_pikkus)
    pen.penup()
    pen.forward(kylje_pikkus * 1.5)
    pen.pendown()

# Lõpeta
pen.hideturtle()
turtle.done()
