liini_pikkus = int(input("Sisesta liini pikkus meetrites (täisarv): "))
maksimaalkaugus = int(input("Sisesta kõrvutiasetsevate postide maksimaalkaugus meetrites (täisarv): "))
posti_arv = (liini_pikkus + maksimaalkaugus - 1) // maksimaalkaugus + 1

print("Liinil on minimaalselt vaja", posti_arv, "posti.")