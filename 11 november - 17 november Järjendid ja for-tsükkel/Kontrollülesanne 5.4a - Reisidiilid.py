# Küsime kasutajalt failinime
failinimi = input("Sisesta failinimi (koos laiendiga, nt sihtkohad.txt): ")

# Avame faili ja loeme andmed
try:
    fail = open(failinimi, encoding="UTF-8")
except FileNotFoundError:
    print("Faili ei leitud. Kontrolli failinime ja proovi uuesti.")
    exit()

# Loeme sihtkohad järjendisse
sihtkohad = []
for rida in fail:
    sihtkohad.append(rida.strip())

# Sulgeme faili
fail.close()

# Näitame kõik sihtkohad koos järjekorranumbritega
for i, sihtkoht in enumerate(sihtkohad, start=1):
    print(f"{i}. {sihtkoht}")

# Küsime kasutajalt, mitmes sihtkoht broneerida
valik = int(input("Sisesta sihtkoha number, mida soovid broneerida: "))

# Kontrollime, kas valik on sobiv
if 1 <= valik <= len(sihtkohad):
    print(f"Oled valinud sihtkoha: {sihtkohad[valik - 1]}")
else:
    print("Vale valik. Proovi uuesti sobiva numbriga.")
