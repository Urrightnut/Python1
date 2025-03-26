def konto_haldur(algne_saldo, toiming, summa):
    """
    Funktsioon pangakonto haldamiseks.
    
    :param algne_saldo: Konto algne saldo.
    :param toiming: 'deposiit' raha lisamiseks või 'valjavote' raha eemaldamiseks.
    :param summa: Summa, mida soovitakse lisada või eemaldada.
    :return: Uus saldo pärast toimingut.
    """
    if toiming == "deposiit":
        algne_saldo += summa
    elif toiming == "valjavote":
        if summa > algne_saldo:
            return "Viga: Ebapiisav saldo!"
        algne_saldo -= summa
    else:
        return "Viga: Tundmatu toiming!"
    
    return algne_saldo

# Näidised
print(konto_haldur(100, "deposiit", 50))   # Väljund: 150
print(konto_haldur(150, "valjavote", 20))  # Väljund: 130
print(konto_haldur(130, "valjavote", 200)) # Väljund: Viga: Ebapiisav saldo!
print(konto_haldur(130, "vale_toiming", 10)) # Väljund: Viga: Tundmatu toiming!
