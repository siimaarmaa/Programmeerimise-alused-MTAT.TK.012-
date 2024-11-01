# Ava fail ja loe andmed järjendisse
fail = open("mopeedid.txt", encoding="UTF-8")

mopeedid = []
for rida in fail:
    mopeedid.append(int(rida))
fail.close()

# Küsime kasutajalt kuu järjekorranumbrit
kuu_number = int(input("Sisesta kuu järjekorranumber (jaanuar 1, veebruar 2 jne): "))

# Kontrollime, et kasutaja sisestus on kehtiv
if 1 <= kuu_number <= 12:
    mopeedide_arv = mopeedid[kuu_number - 1]
    print(f"Sel kuul registreeriti {mopeedide_arv} uut mopeedi.")
else:
    print("Vigane kuu järjekorranumber. Palun sisesta number vahemikus 1 kuni 12.")
