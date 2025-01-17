# Küsime kasutajalt kahe aiaosa pikkused
pikkus1 = float(input("Sisesta esimese aiaosa pikkus meetrites: "))
pikkus2 = float(input("Sisesta teise aiaosa pikkus meetrites: "))

# Arvutame aia kogupikkuse
kogupikkus = 2 * (pikkus1 + pikkus2)

# Väljasta tulemus kasutades f-string vormindamist
print(f"Aia kogupikkus on {kogupikkus} meetrit.")
