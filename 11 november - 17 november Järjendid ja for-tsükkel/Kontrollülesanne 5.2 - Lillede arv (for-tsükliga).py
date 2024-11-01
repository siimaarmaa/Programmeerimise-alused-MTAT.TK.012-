# Küsime kasutajalt klientide arvu
klientide_arv = int(input("Sisesta klientide arv (mittenegatiivne täisarv): "))

# Algväärtustame lillede koguarvu
lillede_koguarv = 0

# Kasutame for-tsüklit ja range() funktsiooni lillede koguarvu arvutamiseks
for i in range(1, klientide_arv + 1, 2):
    lillede_koguarv += i

# Väljastame saadud lillede arvu ekraanile
print(f"Lillede koguarv, mida pood kingib: {lillede_koguarv}")
