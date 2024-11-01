from datetime import datetime

# Funktsioon failist andmete lugemiseks järjendisse
def loe_failist_järjend(failinimi):
    try:
        fail = open(failinimi, encoding="UTF-8")
    except FileNotFoundError:
        print(f"Faili {failinimi} ei leitud. Kontrolli failinime ja proovi uuesti.")
        exit()

    andmed = []
    for rida in fail:
        andmed.append(rida.strip())

    fail.close()
    return andmed

# Küsime kasutajalt failinime
failinimi = input("Sisesta failinimi: ")

# Loeme õpilaste nimed failist järjendisse
nimed = loe_failist_järjend(failinimi)

# Leiame tänase kuupäeva
tana_paev = datetime.now().day

# Väljastame vastava õpilase nime
if tana_paev <= len(nimed):
    print(f"Täna peab vastama: {nimed[tana_paev - 1]}")
else:
    print("Nimekirjas ei ole piisavalt nimesid.")
