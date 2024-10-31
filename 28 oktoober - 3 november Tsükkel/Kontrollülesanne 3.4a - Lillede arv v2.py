# Küsi kasutajalt klientide arvu (mittenegatiivne täisarv)
klientide_arv = int(input("Palun sisesta klientide arv: "))

# Algväärtustame muutujad
lillede_koguarv = 0
praegune_klient = 1
paaritu_arv = 1

# Kasuta while-tsüklit, et arvutada lillede koguarv
while praegune_klient <= klientide_arv:
    lillede_koguarv += paaritu_arv
    paaritu_arv += 2
    praegune_klient += 1

# Väljastame lillede koguarvu ekraanile
print("Pood kingib kokku", lillede_koguarv, "lille.")
