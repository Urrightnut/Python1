import turtle
import math

try:
    # Küsime kasutajalt ringi raadiuse
    raadius = float(input("Sisesta ringi raadius: "))

    if raadius <= 0:
        print("Tegid sisestamisel vea! Raadius peab olema suurem kui 0.")
    else:
        # Arvutame pindala ja ümbermõõdu
        pindala = 3.14 * raadius ** 2
        ymbermoot = 2 * 3.14 * raadius

        # Väljasta tulemus, kasutades f-string vormindamist ja ümardamist 2 komakohta
        print(f"Ringi pindala on {pindala:.2f} ja ümbermõõt on {ymbermoot:.2f}")

        # Loome kilpkonna
        pen = turtle.Turtle()

        # Joonistame ringi
        pen.circle(raadius)

        # Lõpeta
        pen.hideturtle()
        turtle.done()
except ValueError:
    print("Tegid sisestamisel vea! Palun sisesta korrektne arv.")

