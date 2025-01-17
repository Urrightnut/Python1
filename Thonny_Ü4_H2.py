# Defineerime muutujad
tavahind = 12.53
allhindlus = 0.30

# Küsime kasutajalt soovitud raamatute arvu
raamatute_arv = int(input("Sisesta soovitud raamatute arv: "))

# Arvutame soodushinna ja kogumaksumuse
soodushind = tavahind * (1 - allhindlus)
kogumaksumus = raamatute_arv * soodushind

# Väljasta tulemus, kasutades f-string vormindamist ja ümardamist 2 komakohta
print(f"{raamatute_arv} raamatu hind soodustusega on {kogumaksumus:.2f}€.")
