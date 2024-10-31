# Küsi kasutajalt ühe täisarvu (ruudu järjekorranumber malelaual)
ruudu_number = int(input("Palun sisesta ruudu järjekorranumber (1 kuni 64): "))

# Algväärtustame muutujad
nisutera_arv = 1
praegune_ruut = 1

# Kasuta while-tsüklit, et arvutada nisutera arv antud ruudu eest
while praegune_ruut < ruudu_number:
    nisutera_arv *= 2
    praegune_ruut += 1

# Väljastame nisutera arvu ekraanile
print("Ruut nr", ruudu_number, "vajab", nisutera_arv, "nisutera.")
