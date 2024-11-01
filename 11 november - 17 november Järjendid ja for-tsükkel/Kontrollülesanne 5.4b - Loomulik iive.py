# Funktsioon failist andmete lugemiseks ja järjendisse salvestamiseks
def loe_failist_järjend(failinimi):
    try:
        fail = open(failinimi, encoding="UTF-8")
    except FileNotFoundError:
        print(f"Faili {failinimi} ei leitud. Kontrolli failinime ja proovi uuesti.")
        exit()

    andmed = []
    for rida in fail:
        andmed.append(int(rida.strip()))

    fail.close()
    return andmed

# Loeme sündide ja surmade andmed failidest
synnid = loe_failist_järjend("synnid.txt")
surmad = loe_failist_järjend("surmad.txt")

# Arvutame loomuliku iibe
loomulik_iive = []
for i in range(len(synnid)):
    loomulik_iive.append(synnid[i] - surmad[i])

# Väljastame loomuliku iibe järjendi
print("Loomuliku iibe järjend:", loomulik_iive)

# Väljastame kuu numbrid, mille korral oli iive positiivne
positiivse_iibega_kuud = []
for i in range(len(loomulik_iive)):
    if loomulik_iive[i] > 0:
        positiivse_iibega_kuud.append(i + 1)

print("Kuu numbrid, mille korral oli iive positiivne:", positiivse_iibega_kuud)
