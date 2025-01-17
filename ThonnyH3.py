# Loo muutujad
nimi = "Karin"
vanus = 18
keskmine_hinne = 4.7

# Trüki välja lause
print(nimi, ",", vanus, "aastat vana ja keskmine hinne on", keskmine_hinne)



# Loome muutujad
toode = "porgandeid"
kogus = 3
hind = 5.35

# Trükime välja lause, mis ühendab need andmed
print("Soovin " + toode + " " + str(kogus) + ", mille tüki hind on " + str(hind) + " eurot.")


# Loome muutujad
sihtkoht = "Soome"
paevade_arv = 5
oobimise_hind = 30.50

# Trükime välja lause, mis ühendab need andmed
print("Soome reis kestab", paevade_arv, "päeva ja üks öö maksab", oobimise_hind, "eurot.")



# Loome muutujad
raamatu_pealkiri = "Sipsik"
raamatu_autor = "Eno Raud"
raamat = raamatu_pealkiri + " " + raamatu_autor
lehekylgede_arv = 16
hindamisskoor = 9.7

# Trükime välja lause, mis ühendab need andmed
print("Minu lemmikraamat on " + raamat + " , mis on " + str(lehekylgede_arv) + " lehekülge pikk ja mille ma hindan " + str(hindamisskoor) + " punktiga.")



# Loome muutujad
auto_mark = "Eesel"
auto_mudel = "vankriga"
auto = auto_mark + " " + auto_mudel
tootmisaasta = 1996
hind = 150.90

# Trükime välja lause, mis ühendab need andmed
print("Minu unistuste auto on", auto, "aastast", tootmisaasta, "mille hind on", hind, "eurot.")



import turtle

# Loome muutujad
kylje_pikkus = 50
nurk = 90
kujundi_varv = "blue"

# Loome kilpkonna
pen = turtle.Turtle()
pen.color(kujundi_varv)

# Funktsioon ruudu joonistamiseks
def joonista_ruut(pikkus):
    for _ in range(4):
        pen.forward(pikkus)
        pen.right(nurk)

# Alguspunkti seadistamine
pen.penup()
pen.goto(-kylje_pikkus * 1.5, 0)
pen.pendown()

# Joonista 3 ruutu
for i in range(3):
    joonista_ruut(kylje_pikkus)
    pen.penup()
    pen.forward(kylje_pikkus * 1.5)
    pen.pendown()

# Lõpeta
pen.hideturtle()
turtle.done()



