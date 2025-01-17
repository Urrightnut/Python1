try:
    # Küsime kasutajalt, mitu kingitust on vaja pakkida
    kingituste_arv = int(input("Sisesta kingituste arv: "))

    # Arvutame kinkekarpide arvu ja ülejäänud kingituste arvu
    kinkekastid = kingituste_arv // 5
    ulejaak = kingituste_arv % 5

    # Väljasta tulemus, kasutades f-string vormindamist
    print(f"Saad teha {kinkekastid} täis kinkekasti. Üle jääb {ulejaak} kingitust.")
except ValueError:
    print("Tegid sisestamisel vea! Palun sisesta korrektne arv.")
