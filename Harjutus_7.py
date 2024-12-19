#19.12.24
#KevinR
#ülesanne 7

nimi = ["jyri Pootsman","Narva Mari","Maali Seina","Terminaator Juuli kuus lumi on maas"]

#for i in nimi:
#    print(i)
    
for i in range(4):
    print(f"{i+1}. {nimi[i]}")
    
valik = int(input("vali lugu (1-4): "))
print(f"mängin: {nimi[valik-1]}")
#print (nimi[1])