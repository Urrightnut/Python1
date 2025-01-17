try:
    # Küsime kasutajalt faili suurust ja allalaadimiskiirust
    faili_suurus = float(input("Sisesta faili suurus megabaitides (MB): "))
    kiirus = float(input("Sisesta allalaadimiskiirus megabaitides sekundis (MB/s): "))

    # Kontrollime, et allalaadimiskiirus ei ole null või negatiivne
    if kiirus <= 0:
        print("Tegid sisestamisel vea! Allalaadimiskiirus peab olema suurem kui 0.")
    else:
        # Arvutame allalaadimiseks kuluvat aega sekundites
        aeg_sekundites = faili_suurus / kiirus

        # Väljasta tulemus, kasutades f-string vormindamist
        print(f"Allalaadimiseks kulub {aeg_sekundites:.2f} sekundit.")
except ValueError:
    print("Tegid sisestamisel vea! Palun sisesta arvväärtused faili suuruse ja kiiruse jaoks.")
