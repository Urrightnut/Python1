def konto_haldur(algne_saldo, toiming, summa):
    if toiming == 'deposiit':
        algne_saldo += summa
    elif toiming == 'valjavote':
        if summa > algne_saldo:
            return "Viga: Ebapiisav saldo"
        algne_saldo -= summa
    else:
        return "Viga: Tundmatu toiming"
    
    return algne_saldo

if __name__ == "__main__":
    algne_saldo = float(input("Sisesta algne saldo: "))
    while True:
        print("\nVali toiming:")
        print("1 - Deposiit")
        print("2 - Väljavõte")
        print("3 - Lõpeta")
        valik = input("Sisesta valiku number: ")
        
        if valik == '3':
            print("Nägemist!")
            break
        elif valik == '1':
            toiming = 'deposiit'
        elif valik == '2':
            toiming = 'valjavote'
        else:
            print("Viga: Vigane valik")
            continue
        
        summa = float(input("Sisesta summa: "))
        uus_saldo = konto_haldur(algne_saldo, toiming, summa)
        if isinstance(uus_saldo, str):
            print(uus_saldo)
        else:
            algne_saldo = uus_saldo
            print(f"Uus saldo: {algne_saldo}")
