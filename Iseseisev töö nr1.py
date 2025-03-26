import turtle
import math

def joonista_taht(kulje_pikkus, tahtede_arv):
    turtle.speed(0)
    nurk = 360 / tahtede_arv
    for _ in range(tahtede_arv):
        for _ in range(3):  # Kolmnurga joonistamine
            turtle.forward(kulje_pikkus)
            turtle.left(120)
        turtle.left(nurk)  # järgmise kolmnurga asukohta


def pea():
    kulje_pikkus = 100  # Siin saad külje pikkust muuta
    tahtede_arv = 11  # Mustri korduste arv
    
    turtle.penup()
    turtle.goto(-kulje_pikkus / 2, kulje_pikkus / (2 * math.sqrt(3)))
    turtle.pendown()
    
    joonista_taht(kulje_pikkus, tahtede_arv)
    turtle.done()


if __name__ == "__main__":
    pea()
