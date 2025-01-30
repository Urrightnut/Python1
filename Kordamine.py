
#Ülesanded

# print("Tere, maailm!")

# #1.2. Aaasta liblikas
# #4. real luuakse muutuja nimega lause

# aasta = 2020
# liblikas = "teeleht-mosaiikliblikas"
# lause_keskosa = ". aasta liblikas on "
# lause = str(aasta) + lause_keskosa + liblikas
# lause = f"{aasta}{lause_keskosa}{liblikas}"
# print(lause)






# korgus = float(input("sisesta pilvede kõrgus: "))
# if korgus > 6:
#     print("ohoo, on ikka kõrgel!")
# elif korgus >= 2 and korgus <= 6:
#     print("need on tavalised pilved")
# else:
#     print("almusied pilved")




# import math
# inim = 55
# koht = 40

# busside_arv = math.ceil(inim/koht)
# if inim==koht:
#     viimane_inim_arv = inim
# else:
#     viimane_inim_arv = abs(inim - koht)

# print(f"busside arv: {busside_arv}")
# print(f"viimases bussis inimesi: {viimane_inim_arv}")




# kordade_arv = int(input("kordade arv: "))
# for i in range(kordade_arv):
#     print("Tõuse ja sära!")

# i = 0
# while i < kordade_arv:
#     i += 1    
#     print("Tõuse ja sära!")
# else:
#     print("Viga!") 





# porgandid = 0
# ringide_arv = 6

# while ringide_arv > 0:
#     #print(ringide_arv)
#     if ringide_arv % 2 == 0:
#         porgandid += ringide_arv
#     ringide_arv -=1
    
# print(porgandid)







# import random
# ounad = 14
# pp =int(input("mitu pp tahab õuna: "))
# for i in range(pp):
#     suv_oun = random.randint(1, 2)
#     print(suv_oun)
#     ounad -= suv_oun

# print(f"lumivalgekesele jäi {ounad} õuna")
        







# fail = open("rebased.txt", encoding="UTF-8")
# vastuvoetud = []

# for rida in fail:
#     #print(rida, end="")
#     vastuvoetud.append(int(rida))

# fail.close()
# #aasta = 9
# #print(vastuvoetud[aasta-1])

# aasta = input("Lisa aasta 2011-2019: ")
# print(vastuvoetud[int(aasta[3])-1])








# fail = open("konto.txt", encoding="UTF-8")


# for kirje in fail:
#     if float(kirje) > 0:
#         print(float(kirje), end="\n")

# fail.close()





# musa = "edm.txt"
# fail = open("edm.txt", encoding="UTF-8")

# nr = 1
# for pala in fail:
#     print(str(nr)+". "+pala, end="")
#     nr += 1

# print()
# valik = int(input("Vali lugu: "))
# fail = open(musa, encoding="UTF-8") #võib ka: fail.seek(o)
# mangin = 1
# for pala in fail:
#     if valik == mangin:
#         print(pala, end="")
#     mangin+=1
    


# fail.close()





# def liitmine(a, b):
#     # a = 12
#     # b = 14
#     c = a + b
#    # print(c)
#     return c

# nr = 10
# nr2 = 20
# s = liitmine(liitmine(nr, nr2), 100)


def viruvinkel(t1, t2):
    if t1[0]==t2[0]:
        return True
    else:
        return False



def pikim_sona(s):
    sona = ""
    for i in s:
        if len(sona) < len(i):
            sona = i
            print(i)


    print("pikim sõna on: "+sona)
     

sonad = ["viisnurk", "ring", "ruut", "suvaline"]
pikim_sona(sonad)
print(viruvinkel("Mario", "Ets"))
