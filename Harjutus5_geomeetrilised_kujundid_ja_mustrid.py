
 #19.12.2024
#Kevin Riisalu

# Sa oled loomas programmi, mis aitab kontrollida, kas inimesed vastavad vanusepiirangu nõuetele üritusel osalemiseks.
# Programm palub kasutajal sisestada oma vanuse. Kui vanus on vähemalt 18 aastat, siis programm annab teada, et kasutaja võib üritusele siseneda. Kui vanus on alla 18, siis programm teatab, et üritusele sisenemiseks ei ole piisavalt vana.
# Kasuta if ja else lauseid, et luua see vanusekontrolli programm.


# Try:
#     vanus = int(input("anna oma vanus: "))
# if vanus >=18:
#     print ("lubatud")
#     else:
#         print("keelatud")
# except:
#     print("viga sisestuses!")

# Sinu ülesanne on luua lihtne Pythoni programm, mis aitab kasutajal valida sobiva riietuse vastavalt ilmale.
# Kasutaja sisestab temperatuuri (Celsius). Kui temperatuur on alla 0 kraadi, peab programm väljastama soovituse kanda talveriideid. Kui temperatuur on vahemikus 0 kuni 15 kraadi, peaks programm soovitama kanda kevad-sügis rõivaid. Kui temperatuur on üle 15 kraadi, soovitab programm kanda suveriideid.
# Kasuta if, elif ja else lauseid selle ülesande lahendamiseks.

# try:
#     kraadid = 20
#     if kraadid < 0:
#         print ("talveriided")
#     elif kraadid >= 0 and kraadid <= 15:
#         print ("kevad-sügis!")
#     else:
#         print("suvi")
# except:
#         print("viga sisestuses")

# Kirjuta programm, mis kontrollib kasutaja poolt sisestatud vastust lihtsale matemaatikaülesandele.
# Näiteks, programm esitab küsimuse “Mis on 3 korda 4?”. Kasutaja peab sisestama vastuse. Kui kasutaja vastus on 12, siis programm väljastab “Õige vastus!”, kui aga vastus on midagi muud, siis väljastab “Vale vastus, proovi uuesti!”.
# Kasuta if ja else lauseid selleks, et kontrollida kasutaja sisestatud vastust.

import random
import turtle
# 
# try:
#     arv1 = random.randint(1,10)
#     arv2 = random.randint(1,10)
#     vastus = int(intput(f"{arv1} * {arv2} = vastus. \nSisesta vastus"))
#     korrutis = arv1 * arv2
#     print(vastus)
#     print(korrutis)
#     if korrutis == vastus:
#         print("õige")
#     else:
#          print("vale")
#               
# except:
#      print("viga sisestuses!")



try:
    valik = random.randint(0,1)
    arvamus = int(input("vali kull 1 või kiri 0:"))
    if arvamus >=0 and arvamus <=1:
        if valik == arvamus:
            print("arvasid ära")
            turtle.color("green")
            turtle.circle(50)
        
        else:
             print("arvasid valesti")
             turtle.color("red")
             turtle.circle(50)
             turtle.done()
    else:
             print("sellist valikut polnud")
except:
    print("viga sisestuses")
    
